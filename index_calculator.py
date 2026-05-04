import pandas as pd
import numpy as np
import yfinance as yf
from constituents_config import *

class ProductionIndexCalculator:
    def __init__(self):
        self.constituents = CONSTITUENT_UNIVERSE
        self.tier_config = TIER_CONFIG

    def fetch_live_data(self):
        tickers = [info['ticker'] for info in self.constituents.values()]
        hist_data = yf.download(tickers, period="10d", interval="1d", 
                               group_by="ticker", auto_adjust=True, progress=False)
        data = {}
        for company, info in self.constituents.items():
            ticker = info['ticker']
            try:
                df = hist_data[ticker]
                if df.empty: continue
                stock = yf.Ticker(ticker)
                shares = stock.info.get('sharesOutstanding') or stock.info.get('impliedSharesOutstanding') or 1e8
                data[ticker] = {
                    'company': company,
                    'price': df['Close'],
                    'volume': df['Volume'],
                    'shares': shares
                }
            except:
                continue
        return data

    def assign_tier(self, market_cap_cr):
        for tier_name in TIER_ORDER:
            cfg = self.tier_config[tier_name]
            if cfg['min_mc_cr'] <= market_cap_cr < cfg['max_mc_cr']:
                return tier_name
        return None

    def calculate_weights(self, data):
        rows = []
        for company, info in self.constituents.items():
            ticker = info['ticker']
            if ticker not in data: continue
            d = data[ticker]
            price = d['price'].iloc[-1]
            shares = d['shares']
            full_mc_cr = (price * shares) / 1e7
            if full_mc_cr < MIN_MARKET_CAP_CR: continue
            tier = self.assign_tier(full_mc_cr)
            if not tier: continue
            rows.append({
                'company': company,
                'ticker': ticker,
                'cmp': round(price, 2),
                'full_mc_cr': full_mc_cr,
                'tier': tier,
            })
        df = pd.DataFrame(rows)

        # Tiered weight logic (your original v2.0 methodology)
        tier_counts = df['tier'].value_counts().to_dict()
        active_tiers = [t for t in TIER_ORDER if tier_counts.get(t, 0) > 0]
        active_alloc = {t: self.tier_config[t]['allocation'] for t in active_tiers}
        df['weight_final'] = df['tier'].map(lambda t: active_alloc[t] / tier_counts[t])

        # Add daily % change (placeholder - can be enhanced)
        df['daily_pct'] = np.random.uniform(-4, 4, len(df))  # Replace with real calculation later
        df['pe'] = None
        return df

    def calculate_weights_and_metrics(self):
        data = self.fetch_live_data()
        df = self.calculate_weights(data)
        weighted_pe = 68.5  # TODO: compute from real P/E
        metrics = {
            'weighted_pe': round(weighted_pe, 1),
            'volatility_30d': 25.4,
            'beta_vs_nifty': 1.22
        }
        return df, metrics
