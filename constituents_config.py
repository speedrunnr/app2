CONSTITUENT_UNIVERSE = {
    'Eternal (Zomato)': {'ticker': 'ETERNAL.NS', 'free_float_factor': 0.85},
    'Groww': {'ticker': 'GROWW.NS', 'free_float_factor': 0.50},
    'Swiggy': {'ticker': 'SWIGGY.NS', 'free_float_factor': 0.50},
    'Lenskart': {'ticker': 'LENSKART.NS', 'free_float_factor': 0.50},
    'Nykaa': {'ticker': 'NYKAA.NS', 'free_float_factor': 0.48},
    'Info Edge': {'ticker': 'NAUKRI.NS', 'free_float_factor': 0.62},
    'Paytm': {'ticker': 'PAYTM.NS', 'free_float_factor': 1.00},
    'PB Fintech (Policybazaar)': {'ticker': 'POLICYBZR.NS', 'free_float_factor': 0.95},
    'Meesho': {'ticker': 'MEESHO.NS', 'free_float_factor': 0.50},
    'Delhivery': {'ticker': 'DELHIVERY.NS', 'free_float_factor': 0.80},
    'Physics Wallah': {'ticker': 'PWL.NS', 'free_float_factor': 0.50},
    'Digit Insurance': {'ticker': 'GODIGIT.NS', 'free_float_factor': 0.25},
    'Ather Energy': {'ticker': 'ATHERENERG.NS', 'free_float_factor': 0.50},
    'Pine Labs': {'ticker': 'PINELABS.NS', 'free_float_factor': 0.50},
    'Urban Company': {'ticker': 'URBANCO.NS', 'free_float_factor': 0.50},
    'TBO Tek': {'ticker': 'TBOTEK.NS', 'free_float_factor': 0.20},
    'IndiaMart': {'ticker': 'INDIAMART.NS', 'free_float_factor': 0.45},
    'FirstCry': {'ticker': 'FIRSTCRY.NS', 'free_float_factor': 0.30},
    'Ola Electric': {'ticker': 'OLAELEC.NS', 'free_float_factor': 0.20},
    'Blackbuck': {'ticker': 'BLACKBUCK.NS', 'free_float_factor': 0.25},
    'Nazara Tech': {'ticker': 'NAZARA.NS', 'free_float_factor': 0.70},
    'Honasa (Mamaearth)': {'ticker': 'HONASA.NS', 'free_float_factor': 0.65},
    'Aequs': {'ticker': 'AEQUS.NS', 'free_float_factor': 0.50},
    'CarTrade': {'ticker': 'CARTRADE.NS', 'free_float_factor': 0.55},
    'ixigo': {'ticker': 'IXIGO.NS', 'free_float_factor': 0.40},
    'Amagi Media Labs': {'ticker': 'AMAGI.NS', 'free_float_factor': 0.50},
    'WeWork India': {'ticker': 'WEWORK.NS', 'free_float_factor': 0.50},
    'Shadowfax': {'ticker': 'SHADOWFAX.NS', 'free_float_factor': 0.50},
    'Wakefit': {'ticker': 'WAKEFIT.NS', 'free_float_factor': 0.50},
    'MapmyIndia': {'ticker': 'MAPMYINDIA.NS', 'free_float_factor': 0.47},
    'Bluestone': {'ticker': 'BLUESTONE.NS', 'free_float_factor': 0.50},
    'Avenues AI': {'ticker': 'CCAVENUE.NS', 'free_float_factor': 0.70},
    'Rategain': {'ticker': 'RATEGAIN.NS', 'free_float_factor': 0.45},
    'Justdial': {'ticker': 'JUSTDIAL.NS', 'free_float_factor': 0.25},
    'Smartworks': {'ticker': 'SMARTWORKS.NS', 'free_float_factor': 0.50},
    'E2E Networks': {'ticker': 'E2E.NS', 'free_float_factor': 0.35},
    'Capillary Technologies': {'ticker': 'CAPILLARY.NS', 'free_float_factor': 0.50},
    'Zaggle': {'ticker': 'ZAGGLE.NS', 'free_float_factor': 0.30},
    'Indiqube Spaces': {'ticker': 'INDIQUBE.NS', 'free_float_factor': 0.50},
    'Yatra': {'ticker': 'YATRA.NS', 'free_float_factor': 0.40},
    'Easemytrip': {'ticker': 'EASEMYTRIP.NS', 'free_float_factor': 0.28},
    'Awfis': {'ticker': 'AWFIS.NS', 'free_float_factor': 0.30},
    'FINO Payment Bank': {'ticker': 'FINOPB.NS', 'free_float_factor': 0.75},
    'Ideaforge': {'ticker': 'IDEAFORGE.NS', 'free_float_factor': 0.30},
    'Mobikwik': {'ticker': 'MOBIKWIK.NS', 'free_float_factor': 0.30},
    'Unicommerce': {'ticker': 'UNIECOM.NS', 'free_float_factor': 0.25},
    'Matrimony': {'ticker': 'MATRIMONY.NS', 'free_float_factor': 0.48}
}

TIER_CONFIG = {
    'Large': {'min_mc_cr': 50000, 'max_mc_cr': float('inf'), 'allocation': 0.50},
    'Mid':   {'min_mc_cr': 10000, 'max_mc_cr': 50000,        'allocation': 0.35},
    'Small': {'min_mc_cr':  1000, 'max_mc_cr': 10000,        'allocation': 0.15},
}

TIER_ORDER = ['Large', 'Mid', 'Small']
TIER_COLORS = {'Large': '#2E86AB', 'Mid': '#F18F01', 'Small': '#06A77D'}

MIN_MARKET_CAP_CR = 1000.0
MIN_ADTV_CRORES = 5.0
