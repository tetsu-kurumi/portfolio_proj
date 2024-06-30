# %% [markdown]
# ## Installing Dependencies
# - yahooquery
# - pandas
# - numpy
# - scikit-learn

# %%
from yahooquery import Ticker
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import math
import sys
import warnings
import json

# Suppress FutureWarnings
warnings.filterwarnings("ignore", category=FutureWarning)

# %% [markdown]
# ## Setting Global Variables

# %%
# EDIT THIS PART IF INITIALIZING YOURSELF
OUTPUT_FILE = 'Initialization.json'

INCOME_DICT = {}
GROWTH_DICT = {}
DEFAULT_DICT = {}
ESG_DICT = {}

DEFAULT_RANKING = {}
INCOME_RANKING = {}
GROWTH_RANKING = {}
ESG_RANKING = {}

DEFAULT_RANKING_LIST = []
INCOME_RANKING_LIST = []
GROWTH_RANKING_LIST = []
ESG_RANKING_LIST = []

# %%
# GLOBAL VARIABLES

SP_LIST = ['MMM', 'AOS', 'ABT', 'ABBV', 'ACN', 'ADBE', 'AMD', 'AES', 'AFL', 'A', 'APD', 'ABNB', 'AKAM', 'ALB', 'ARE', 'ALGN', 'ALLE', 'LNT', 'ALL', 'GOOGL', 'GOOG', 'MO', 'AMZN', 'AMCR', 'AEE', 'AAL', 'AEP', 'AXP', 'AIG', 'AMT', 'AWK', 'AMP', 'AME', 'AMGN', 'APH', 'ADI', 'ANSS', 'AON', 'APA', 'AAPL', 'AMAT', 'APTV', 'ACGL', 'ADM', 'ANET', 'AJG', 'AIZ', 'T', 'ATO', 'ADSK', 'ADP', 'AZO', 'AVB', 'AVY', 'AXON', 'BKR', 'BALL', 'BAC', 'BK', 'BBWI', 'BAX', 'BDX', 'BRK-B', 'BBY', 'BIO', 'TECH', 'BIIB', 'BLK', 'BX', 'BA', 'BKNG', 'BWA', 'BXP', 'BSX', 'BMY', 'AVGO', 'BR', 'BRO', 'BF-B', 'BLDR', 'BG', 'CDNS', 'CZR', 'CPT', 'CPB', 'COF', 'CAH', 'KMX', 'CCL', 'CARR', 'CTLT', 'CAT', 'CBOE', 'CBRE', 'CDW', 'CE', 'COR', 'CNC', 'CNP', 'CF', 'CHRW', 'CRL', 'SCHW', 'CHTR', 'CVX', 'CMG', 'CB', 'CHD', 'CI', 'CINF', 'CTAS', 'CSCO', 'C', 'CFG', 'CLX', 'CME', 'CMS', 'KO', 'CTSH', 'CL', 'CMCSA', 'CMA', 'CAG', 'COP', 'ED', 'STZ', 'CEG', 'COO', 'CPRT', 'GLW', 'CTVA', 'CSGP', 'COST', 'CTRA', 'CCI', 'CSX', 'CMI', 'CVS', 'DHR', 'DRI', 'DVA', 'DAY', 'DE', 'DAL', 'XRAY', 'DVN', 'DXCM', 'FANG', 'DLR', 'DFS', 'DG', 'DLTR', 'D', 'DPZ', 'DOV', 'DOW', 'DHI', 'DTE', 'DUK', 'DD', 'EMN', 'ETN', 'EBAY', 'ECL', 'EIX', 'EW', 'EA', 'ELV', 'LLY', 'EMR', 'ENPH', 'ETR', 'EOG', 'EPAM', 'EQT', 'EFX', 'EQIX', 'EQR', 'ESS', 'EL', 'ETSY', 'EG', 'EVRG', 'ES', 'EXC', 'EXPE', 'EXPD', 'EXR', 'XOM', 'FFIV', 'FDS', 'FICO', 'FAST', 'FRT', 'FDX', 'FIS', 'FITB', 'FSLR', 'FE', 'FI', 'FLT', 'FMC', 'F', 'FTNT', 'FTV', 'FOXA', 'FOX', 'BEN', 'FCX', 'GRMN', 'IT', 'GEHC', 'GEN', 'GNRC', 'GD', 'GE', 'GIS', 'GM', 'GPC', 'GILD', 'GPN', 'GL', 'GS', 'HAL', 'HIG', 'HAS', 'HCA', 'DOC', 'HSIC', 'HSY', 'HES', 'HPE', 'HLT', 'HOLX', 'HD', 'HON', 'HRL', 'HST', 'HWM', 'HPQ', 'HUBB', 'HUM', 'HBAN', 'HII', 'IBM', 'IEX', 'IDXX', 'ITW', 'ILMN', 'INCY', 'IR', 'PODD', 'INTC', 'ICE', 'IFF', 'IP', 'IPG', 'INTU', 'ISRG', 'IVZ', 'INVH', 'IQV', 'IRM', 'JBHT', 'JBL', 'JKHY', 'J', 'JNJ', 'JCI', 'JPM', 'JNPR', 'K', 'KVUE', 'KDP', 'KEY', 'KEYS', 'KMB', 'KIM', 'KMI', 'KLAC', 'KHC', 'KR', 'LHX', 'LH', 'LRCX', 'LW', 'LVS', 'LDOS', 'LEN', 'LIN', 'LYV', 'LKQ', 'LMT', 'L', 'LOW', 'LULU', 'LYB', 'MTB', 'MRO', 'MPC', 'MKTX', 'MAR', 'MMC', 'MLM', 'MAS', 'MA', 'MTCH', 'MKC', 'MCD', 'MCK', 'MDT', 'MRK', 'META', 'MET', 'MTD', 'MGM', 'MCHP', 'MU', 'MSFT', 'MAA', 'MRNA', 'MHK', 'MOH', 'TAP', 'MDLZ', 'MPWR', 'MNST', 'MCO', 'MS', 'MOS', 'MSI', 'MSCI', 'NDAQ', 'NTAP', 'NFLX', 'NEM', 'NWSA', 'NWS', 'NEE', 'NKE', 'NI', 'NDSN', 'NSC', 'NTRS', 'NOC', 'NCLH', 'NRG', 'NUE', 'NVDA', 'NVR', 'NXPI', 'ORLY', 'OXY', 'ODFL', 'OMC', 'ON', 'OKE', 'ORCL', 'OTIS', 'PCAR', 'PKG', 'PANW', 'PARA', 'PH', 'PAYX', 'PAYC', 'PYPL', 'PNR', 'PEP', 'PFE', 'PCG', 'PM', 'PSX', 'PNW', 'PXD', 'PNC', 'POOL', 'PPG', 'PPL', 'PFG', 'PG', 'PGR', 'PLD', 'PRU', 'PEG', 'PTC', 'PSA', 'PHM', 'QRVO', 'PWR', 'QCOM', 'DGX', 'RL', 'RJF', 'RTX', 'O', 'REG', 'REGN', 'RF', 'RSG', 'RMD', 'RVTY', 'RHI', 'ROK', 'ROL', 'ROP', 'ROST', 'RCL', 'SPGI', 'CRM', 'SBAC', 'SLB', 'STX', 'SRE', 'NOW', 'SHW', 'SPG', 'SWKS', 'SJM', 'SNA', 'SO', 'LUV', 'SWK', 'SBUX', 'STT', 'STLD', 'STE', 'SYK', 'SYF', 'SNPS', 'SYY', 'TMUS', 'TROW', 'TTWO', 'TPR', 'TRGP', 'TGT', 'TEL', 'TDY', 'TFX', 'TER', 'TSLA', 'TXN', 'TXT', 'TMO', 'TJX', 'TSCO', 'TT', 'TDG', 'TRV', 'TRMB', 'TFC', 'TYL', 'TSN', 'USB', 'UBER', 'UDR', 'ULTA', 'UNP', 'UAL', 'UPS', 'URI', 'UNH', 'UHS', 'VLO', 'VTR', 'VLTO', 'VRSN', 'VRSK', 'VZ', 'VRTX', 'VFC', 'VTRS', 'VICI', 'V', 'VMC', 'WRB', 'WAB', 'WBA', 'WMT', 'DIS', 'WBD', 'WM', 'WAT', 'WEC', 'WFC', 'WELL', 'WST', 'WDC', 'WRK', 'WY', 'WHR', 'WMB', 'WTW', 'GWW', 'WYNN', 'XEL', 'XYL', 'YUM', 'ZBRA', 'ZBH', 'ZION', 'ZTS']
STOCK_SECTOR_DICT = {'MMM': 'Industrials', 'AOS': 'Industrials', 'ABT': 'Healthcare', 'ABBV': 'Healthcare', 'ACN': 'Technology', 'ADBE': 'Technology', 'AMD': 'Technology', 'AES': 'Utilities', 'AFL': 'Financial Services', 'A': 'Healthcare', 'APD': 'Basic Materials', 'ABNB': 'Consumer Cyclical', 'AKAM': 'Technology', 'ALB': 'Basic Materials', 'ARE': 'Real Estate', 'ALGN': 'Healthcare', 'ALLE': 'Industrials', 'LNT': 'Utilities', 'ALL': 'Financial Services', 'GOOGL': 'Communication Services', 'GOOG': 'Communication Services', 'MO': 'Consumer Defensive', 'AMZN': 'Consumer Cyclical', 'AMCR': 'Consumer Cyclical', 'AEE': 'Utilities', 'AAL': 'Industrials', 'AEP': 'Utilities', 'AXP': 'Financial Services', 'AIG': 'Financial Services', 'AMT': 'Real Estate', 'AWK': 'Utilities', 'AMP': 'Financial Services', 'AME': 'Industrials', 'AMGN': 'Healthcare', 'APH': 'Technology', 'ADI': 'Technology', 'ANSS': 'Technology', 'AON': 'Financial Services', 'APA': 'Energy', 'AAPL': 'Technology', 'AMAT': 'Technology', 'APTV': 'Consumer Cyclical', 'ACGL': 'Financial Services', 'ADM': 'Consumer Defensive', 'ANET': 'Technology', 'AJG': 'Financial Services', 'AIZ': 'Financial Services', 'T': 'Communication Services', 'ATO': 'Utilities', 'ADSK': 'Technology', 'ADP': 'Industrials', 'AZO': 'Consumer Cyclical', 'AVB': 'Real Estate', 'AVY': 'Consumer Cyclical', 'AXON': 'Industrials', 'BKR': 'Energy', 'BALL': 'Consumer Cyclical', 'BAC': 'Financial Services', 'BK': 'Financial Services', 'BBWI': 'Consumer Cyclical', 'BAX': 'Healthcare', 'BDX': 'Healthcare', 'BRK-B': 'Financial Services', 'BBY': 'Consumer Cyclical', 'BIO': 'Healthcare', 'TECH': 'Healthcare', 'BIIB': 'Healthcare', 'BLK': 'Financial Services', 'BX': 'Financial Services', 'BA': 'Industrials', 'BKNG': 'Consumer Cyclical', 'BWA': 'Consumer Cyclical', 'BXP': 'Real Estate', 'BSX': 'Healthcare', 'BMY': 'Healthcare', 'AVGO': 'Technology', 'BR': 'Technology', 'BRO': 'Financial Services', 'BF-B': 'Consumer Defensive', 'BLDR': 'Industrials', 'BG': 'Consumer Defensive', 'CDNS': 'Technology', 'CZR': 'Consumer Cyclical', 'CPT': 'Real Estate', 'CPB': 'Consumer Defensive', 'COF': 'Financial Services', 'CAH': 'Healthcare', 'KMX': 'Consumer Cyclical', 'CCL': 'Consumer Cyclical', 'CARR': 'Industrials', 'CTLT': 'Healthcare', 'CAT': 'Industrials', 'CBOE': 'Financial Services', 'CBRE': 'Real Estate', 'CDW': 'Technology', 'CE': 'Basic Materials', 'COR': 'Healthcare', 'CNC': 'Healthcare', 'CNP': 'Utilities', 'CF': 'Basic Materials', 'CHRW': 'Industrials', 'CRL': 'Healthcare', 'SCHW': 'Financial Services', 'CHTR': 'Communication Services', 'CVX': 'Energy', 'CMG': 'Consumer Cyclical', 'CB': 'Financial Services', 'CHD': 'Consumer Defensive', 'CI': 'Healthcare', 'CINF': 'Financial Services', 'CTAS': 'Industrials', 'CSCO': 'Technology', 'C': 'Financial Services', 'CFG': 'Financial Services', 'CLX': 'Consumer Defensive', 'CME': 'Financial Services', 'CMS': 'Utilities', 'KO': 'Consumer Defensive', 'CTSH': 'Technology', 'CL': 'Consumer Defensive', 'CMCSA': 'Communication Services', 'CMA': 'Financial Services', 'CAG': 'Consumer Defensive', 'COP': 'Energy', 'ED': 'Utilities', 'STZ': 'Consumer Defensive', 'CEG': 'Utilities', 'COO': 'Healthcare', 'CPRT': 'Industrials', 'GLW': 'Technology', 'CTVA': 'Basic Materials', 'CSGP': 'Real Estate', 'COST': 'Consumer Defensive', 'CTRA': 'Energy', 'CCI': 'Real Estate', 'CSX': 'Industrials', 'CMI': 'Industrials', 'CVS': 'Healthcare', 'DHR': 'Healthcare', 'DRI': 'Consumer Cyclical', 'DVA': 'Healthcare', 'DAY': 'Technology', 'DE': 'Industrials', 'DAL': 'Industrials', 'XRAY': 'Healthcare', 'DVN': 'Energy', 'DXCM': 'Healthcare', 'FANG': 'Energy', 'DLR': 'Real Estate', 'DFS': 'Financial Services', 'DG': 'Consumer Defensive', 'DLTR': 'Consumer Defensive', 'D': 'Utilities', 'DPZ': 'Consumer Cyclical', 'DOV': 'Industrials', 'DOW': 'Basic Materials', 'DHI': 'Consumer Cyclical', 'DTE': 'Utilities', 'DUK': 'Utilities', 'DD': 'Basic Materials', 'EMN': 'Basic Materials', 'ETN': 'Industrials', 'EBAY': 'Consumer Cyclical', 'ECL': 'Basic Materials', 'EIX': 'Utilities', 'EW': 'Healthcare', 'EA': 'Communication Services', 'ELV': 'Healthcare', 'LLY': 'Healthcare', 'EMR': 'Industrials', 'ENPH': 'Technology', 'ETR': 'Utilities', 'EOG': 'Energy', 'EPAM': 'Technology', 'EQT': 'Energy', 'EFX': 'Industrials', 'EQIX': 'Real Estate', 'EQR': 'Real Estate', 'ESS': 'Real Estate', 'EL': 'Consumer Defensive', 'ETSY': 'Consumer Cyclical', 'EG': 'Financial Services', 'EVRG': 'Utilities', 'ES': 'Utilities', 'EXC': 'Utilities', 'EXPE': 'Consumer Cyclical', 'EXPD': 'Industrials', 'EXR': 'Real Estate', 'XOM': 'Energy', 'FFIV': 'Technology', 'FDS': 'Financial Services', 'FICO': 'Technology', 'FAST': 'Industrials', 'FRT': 'Real Estate', 'FDX': 'Industrials', 'FIS': 'Technology', 'FITB': 'Financial Services', 'FSLR': 'Technology', 'FE': 'Utilities', 'FI': 'Technology', 'FLT': 'Technology', 'FMC': 'Basic Materials', 'F': 'Consumer Cyclical', 'FTNT': 'Technology', 'FTV': 'Technology', 'FOXA': 'Communication Services', 'FOX': 'Communication Services', 'BEN': 'Financial Services', 'FCX': 'Basic Materials', 'GRMN': 'Technology', 'IT': 'Technology', 'GEHC': 'Healthcare', 'GEN': 'Technology', 'GNRC': 'Industrials', 'GD': 'Industrials', 'GE': 'Industrials', 'GIS': 'Consumer Defensive', 'GM': 'Consumer Cyclical', 'GPC': 'Consumer Cyclical', 'GILD': 'Healthcare', 'GPN': 'Industrials', 'GL': 'Financial Services', 'GS': 'Financial Services', 'HAL': 'Energy', 'HIG': 'Financial Services', 'HAS': 'Consumer Cyclical', 'HCA': 'Healthcare', 'DOC': 'Real Estate', 'HSIC': 'Healthcare', 'HSY': 'Consumer Defensive', 'HES': 'Energy', 'HPE': 'Technology', 'HLT': 'Consumer Cyclical', 'HOLX': 'Healthcare', 'HD': 'Consumer Cyclical', 'HON': 'Industrials', 'HRL': 'Consumer Defensive', 'HST': 'Real Estate', 'HWM': 'Industrials', 'HPQ': 'Technology', 'HUBB': 'Industrials', 'HUM': 'Healthcare', 'HBAN': 'Financial Services', 'HII': 'Industrials', 'IBM': 'Technology', 'IEX': 'Industrials', 'IDXX': 'Healthcare', 'ITW': 'Industrials', 'ILMN': 'Healthcare', 'INCY': 'Healthcare', 'IR': 'Industrials', 'PODD': 'Healthcare', 'INTC': 'Technology', 'ICE': 'Financial Services', 'IFF': 'Basic Materials', 'IP': 'Consumer Cyclical', 'IPG': 'Communication Services', 'INTU': 'Technology', 'ISRG': 'Healthcare', 'IVZ': 'Financial Services', 'INVH': 'Real Estate', 'IQV': 'Healthcare', 'IRM': 'Real Estate', 'JBHT': 'Industrials', 'JBL': 'Technology', 'JKHY': 'Technology', 'J': 'Industrials', 'JNJ': 'Healthcare', 'JCI': 'Industrials', 'JPM': 'Financial Services', 'JNPR': 'Technology', 'K': 'Consumer Defensive', 'KVUE': 'Consumer Defensive', 'KDP': 'Consumer Defensive', 'KEY': 'Financial Services', 'KEYS': 'Technology', 'KMB': 'Consumer Defensive', 'KIM': 'Real Estate', 'KMI': 'Energy', 'KLAC': 'Technology', 'KHC': 'Consumer Defensive', 'KR': 'Consumer Defensive', 'LHX': 'Industrials', 'LH': 'Healthcare', 'LRCX': 'Technology', 'LW': 'Consumer Defensive', 'LVS': 'Consumer Cyclical', 'LDOS': 'Technology', 'LEN': 'Consumer Cyclical', 'LIN': 'Basic Materials', 'LYV': 'Communication Services', 'LKQ': 'Consumer Cyclical', 'LMT': 'Industrials', 'L': 'Financial Services', 'LOW': 'Consumer Cyclical', 'LULU': 'Consumer Cyclical', 'LYB': 'Basic Materials', 'MTB': 'Financial Services', 'MRO': 'Energy', 'MPC': 'Energy', 'MKTX': 'Financial Services', 'MAR': 'Consumer Cyclical', 'MMC': 'Financial Services', 'MLM': 'Basic Materials', 'MAS': 'Industrials', 'MA': 'Financial Services', 'MTCH': 'Communication Services', 'MKC': 'Consumer Defensive', 'MCD': 'Consumer Cyclical', 'MCK': 'Healthcare', 'MDT': 'Healthcare', 'MRK': 'Healthcare', 'META': 'Communication Services', 'MET': 'Financial Services', 'MTD': 'Healthcare', 'MGM': 'Consumer Cyclical', 'MCHP': 'Technology', 'MU': 'Technology', 'MSFT': 'Technology', 'MAA': 'Real Estate', 'MRNA': 'Healthcare', 'MHK': 'Consumer Cyclical', 'MOH': 'Healthcare', 'TAP': 'Consumer Defensive', 'MDLZ': 'Consumer Defensive', 'MPWR': 'Technology', 'MNST': 'Consumer Defensive', 'MCO': 'Financial Services', 'MS': 'Financial Services', 'MOS': 'Basic Materials', 'MSI': 'Technology', 'MSCI': 'Financial Services', 'NDAQ': 'Financial Services', 'NTAP': 'Technology', 'NFLX': 'Communication Services', 'NEM': 'Basic Materials', 'NWSA': 'Communication Services', 'NWS': 'Communication Services', 'NEE': 'Utilities', 'NKE': 'Consumer Cyclical', 'NI': 'Utilities', 'NDSN': 'Industrials', 'NSC': 'Industrials', 'NTRS': 'Financial Services', 'NOC': 'Industrials', 'NCLH': 'Consumer Cyclical', 'NRG': 'Utilities', 'NUE': 'Basic Materials', 'NVDA': 'Technology', 'NVR': 'Consumer Cyclical', 'NXPI': 'Technology', 'ORLY': 'Consumer Cyclical', 'OXY': 'Energy', 'ODFL': 'Industrials', 'OMC': 'Communication Services', 'ON': 'Technology', 'OKE': 'Energy', 'ORCL': 'Technology', 'OTIS': 'Industrials', 'PCAR': 'Industrials', 'PKG': 'Consumer Cyclical', 'PANW': 'Technology', 'PARA': 'Communication Services', 'PH': 'Industrials', 'PAYX': 'Industrials', 'PAYC': 'Technology', 'PYPL': 'Financial Services', 'PNR': 'Industrials', 'PEP': 'Consumer Defensive', 'PFE': 'Healthcare', 'PCG': 'Utilities', 'PM': 'Consumer Defensive', 'PSX': 'Energy', 'PNW': 'Utilities', 'PXD': 'Energy', 'PNC': 'Financial Services', 'POOL': 'Industrials', 'PPG': 'Basic Materials', 'PPL': 'Utilities', 'PFG': 'Financial Services', 'PG': 'Consumer Defensive', 'PGR': 'Financial Services', 'PLD': 'Real Estate', 'PRU': 'Financial Services', 'PEG': 'Utilities', 'PTC': 'Technology', 'PSA': 'Real Estate', 'PHM': 'Consumer Cyclical', 'QRVO': 'Technology', 'PWR': 'Industrials', 'QCOM': 'Technology', 'DGX': 'Healthcare', 'RL': 'Consumer Cyclical', 'RJF': 'Financial Services', 'RTX': 'Industrials', 'O': 'Real Estate', 'REG': 'Real Estate', 'REGN': 'Healthcare', 'RF': 'Financial Services', 'RSG': 'Industrials', 'RMD': 'Healthcare', 'RVTY': 'Healthcare', 'RHI': 'Industrials', 'ROK': 'Industrials', 'ROL': 'Consumer Cyclical', 'ROP': 'Technology', 'ROST': 'Consumer Cyclical', 'RCL': 'Consumer Cyclical', 'SPGI': 'Financial Services', 'CRM': 'Technology', 'SBAC': 'Real Estate', 'SLB': 'Energy', 'STX': 'Technology', 'SRE': 'Utilities', 'NOW': 'Technology', 'SHW': 'Basic Materials', 'SPG': 'Real Estate', 'SWKS': 'Technology', 'SJM': 'Consumer Defensive', 'SNA': 'Industrials', 'SO': 'Utilities', 'LUV': 'Industrials', 'SWK': 'Industrials', 'SBUX': 'Consumer Cyclical', 'STT': 'Financial Services', 'STLD': 'Basic Materials', 'STE': 'Healthcare', 'SYK': 'Healthcare', 'SYF': 'Financial Services', 'SNPS': 'Technology', 'SYY': 'Consumer Defensive', 'TMUS': 'Communication Services', 'TROW': 'Financial Services', 'TTWO': 'Communication Services', 'TPR': 'Consumer Cyclical', 'TRGP': 'Energy', 'TGT': 'Consumer Defensive', 'TEL': 'Technology', 'TDY': 'Technology', 'TFX': 'Healthcare', 'TER': 'Technology', 'TSLA': 'Consumer Cyclical', 'TXN': 'Technology', 'TXT': 'Industrials', 'TMO': 'Healthcare', 'TJX': 'Consumer Cyclical', 'TSCO': 'Consumer Cyclical', 'TT': 'Industrials', 'TDG': 'Industrials', 'TRV': 'Financial Services', 'TRMB': 'Technology', 'TFC': 'Financial Services', 'TYL': 'Technology', 'TSN': 'Consumer Defensive', 'USB': 'Financial Services', 'UBER': 'Technology', 'UDR': 'Real Estate', 'ULTA': 'Consumer Cyclical', 'UNP': 'Industrials', 'UAL': 'Industrials', 'UPS': 'Industrials', 'URI': 'Industrials', 'UNH': 'Healthcare', 'UHS': 'Healthcare', 'VLO': 'Energy', 'VTR': 'Real Estate', 'VLTO': 'Industrials', 'VRSN': 'Technology', 'VRSK': 'Industrials', 'VZ': 'Communication Services', 'VRTX': 'Healthcare', 'VFC': 'Consumer Cyclical', 'VTRS': 'Healthcare', 'VICI': 'Real Estate', 'V': 'Financial Services', 'VMC': 'Basic Materials', 'WRB': 'Financial Services', 'WAB': 'Industrials', 'WBA': 'Healthcare', 'WMT': 'Consumer Defensive', 'DIS': 'Communication Services', 'WBD': 'Communication Services', 'WM': 'Industrials', 'WAT': 'Healthcare', 'WEC': 'Utilities', 'WFC': 'Financial Services', 'WELL': 'Real Estate', 'WST': 'Healthcare', 'WDC': 'Technology', 'WRK': 'Consumer Cyclical', 'WY': 'Real Estate', 'WHR': 'Consumer Cyclical', 'WMB': 'Energy', 'WTW': 'Financial Services', 'GWW': 'Industrials', 'WYNN': 'Consumer Cyclical', 'XEL': 'Utilities', 'XYL': 'Industrials', 'YUM': 'Consumer Cyclical', 'ZBRA': 'Technology', 'ZBH': 'Healthcare', 'ZION': 'Financial Services', 'ZTS': 'Healthcare'}

# Ref: https://pages.stern.nyu.edu/~adamodar/New_Home_Page/datafile/wacc.htm and https://www.linkedin.com/pulse/sp-500-sectors-roic-vs-wacc-through-1q21-david-trainer/
WACC_RATES = {
    'Technology': 0.092,
    'Healthcare': 0.1028,
    'Financial Services': 0.1,
    'Consumer Cyclical': 0.0786,
    'Consumer Defensive': 0.07,
    'Industrials': 0.0791,
    'Energy': 0.0867,
    'Utilities': 0.068,
    'Basic Materials': 0.08,
    'Real Estate': 0.0986,
    'Communication Services': 0.073,
}

SECTORS = list(WACC_RATES.keys())

MARKETCAPS = ['largecap', 'midcap', 'smallcap']

# (See Appendix A for source code to obtain data)
AVGPERATIOS = {'Technology': {'largecap': 30.059571877038476, 'midcap': 23.431135714285713, 'smallcap': 23.431135714285713}, 'Healthcare': {'largecap': 26.132716674737697, 'midcap': 19.027188333333335, 'smallcap': 19.027188333333335}, 'Financial Services': {'largecap': 14.642611246031754, 'midcap': 13.60500992063492, 'smallcap': 13.60500992063492}, 'Consumer Cyclical': {'largecap': 23.29654477678572, 'midcap': 15.738475571428575, 'smallcap': 15.738475571428575}, 'Consumer Defensive': {'largecap': 20.204181280566274, 'midcap': 20.204181280566274, 'smallcap': 20.204181280566274}, 'Industrials': {'largecap': 29.380842490223145, 'midcap': 16.044789761904763, 'smallcap': 16.044789761904763}, 'Energy': {'largecap': 12.821854865424433, 'midcap': 12.821854865424433, 'smallcap': 12.821854865424433}, 'Utilities': {'largecap': 16.451003965517234, 'midcap': 16.90904, 'smallcap': 16.90904}, 'Basic Materials': {'largecap': 18.409827839285715, 'midcap': 11.088911666666666, 'smallcap': 11.088911666666666}, 'Real Estate': {'largecap': 44.37390593537415, 'midcap': 29.754506666666664, 'smallcap': 29.754506666666664}, 'Communication Services': {'largecap': 22.433460565476192, 'midcap': 14.81876, 'smallcap': 14.81876}}

# AVGPERATIOS = {'Technology': 49.23658881690141,
#  'Healthcare': 56.14869727118644,
#  'Financial Services': 19.586146538461545,
#  'Consumer Cyclical': 24.644157226415093,
#  'Consumer Defensive': 31.269938114285708,
#  'Industrials': 30.180891085714283,
#  'Energy': 13.010462826086957,
#  'Utilities': 19.340905928571427,
#  'Basic Materials': 26.606018799999998,
#  'Real Estate': 50.20442143333334,
#  'Communication Services': 30.231775736842103}

# Assumed average growth rate for entire market
GROWTH_RATE = 0.04

# Default variables if the user inputs stocks in sectors that were not expected
DEFAULT_WACC_RATE = 0.084
DEFAULT_PE_RATIO = 31.6

# (See Appendix B for source code to obtain data)
AVGUPSIDES = {'Technology': {'largecap': -0.4295610250928806, 'midcap': -0.38983803209391904, 'smallcap': -0.38983803209391904}, 'Healthcare': {'largecap': -0.38059532968374693, 'midcap': -0.5249137166756629, 'smallcap': -0.5249137166756629}, 'Financial Services': {'largecap': 0.3090236329278931, 'midcap': 0.9697741321195159, 'smallcap': 0.9697741321195159}, 'Consumer Cyclical': {'largecap': 0.11011095192734544, 'midcap': -0.3573431004186485, 'smallcap': -0.3573431004186485}, 'Consumer Defensive': {'largecap': 0.3684461717667686, 'midcap': 0.3684461717667686, 'smallcap': 0.3684461717667686}, 'Industrials': {'largecap': -0.17008348305991614, 'midcap': 0.9078278862153412, 'smallcap': 0.9078278862153412}, 'Energy': {'largecap': 0.4231101378788156, 'midcap': 0.4231101378788156, 'smallcap': 0.4231101378788156}, 'Utilities': {'largecap': -2.4520807347139253, 'midcap': -3.356112980041267, 'smallcap': -3.356112980041267}, 'Basic Materials': {'largecap': -0.03333269456157282, 'midcap': -2.532044696879707, 'smallcap': -2.532044696879707}, 'Real Estate': {'largecap': -0.31494003752253263, 'midcap': 0.20814410550156637, 'smallcap': 0.20814410550156637}, 'Communication Services': {'largecap': 1.412481580819086, 'midcap': 0.5989914761265078, 'smallcap': 0.5989914761265078}}
# {'Technology': {'largecap': -0.46532794252636306, 'midcap': -0.21392046923820554, 'smallcap': -0.21392046923820554}, 'Healthcare': {'largecap': -0.43055560930173425, 'midcap': -0.5719170423212125, 'smallcap': -0.21392046923820554}, 'Financial Services': {'largecap': 0.3029707379229806, 'midcap': 0.6715045600325802, 'smallcap': -0.21392046923820554}, 'Consumer Cyclical': {'largecap': 0.08440235744354845, 'midcap': -0.4348427886408699, 'smallcap': -0.21392046923820554}, 'Consumer Defensive': {'largecap': -0.2158942523257203, 'midcap': -0.21392046923820554, 'smallcap': -0.21392046923820554}, 'Industrials': {'largecap': -0.19325612805530254, 'midcap': 0.8031396239132172, 'smallcap': -0.21392046923820554}, 'Energy': {'largecap': 0.510275576264435, 'midcap': 0.5326022958942742, 'smallcap': -0.21392046923820554}, 'Utilities': {'largecap': -2.544612808703413, 'midcap': -3.427366258394338, 'smallcap': -0.21392046923820554}, 'Basic Materials': {'largecap': -0.06398120906354324, 'midcap': -2.4225627087099912, 'smallcap': -0.21392046923820554}, 'Real Estate': {'largecap': -0.3261417740317038, 'midcap': 0.9050036015731132, 'smallcap': -0.21392046923820554}, 'Communication Services': {'largecap': 1.343112974529212, 'midcap': 0.4747008587111436, 'smallcap': -0.21392046923820554}}

STARTDATE_LIST = ['2014-01-01', '2015-01-01', '2016-01-01', '2017-01-01', '2018-01-01'
                  '2019-01-01', '2020-01-01', '2021-01-01', '2022-01-01', '2023-01-01', '2024-01-01']

json_dict = {}
# %% [markdown]
# ## class GetInfo
# This class accesses yahooquery and returns information 
# 
# When there is no information available, it returns nan so that subsequent calculations can be performed and the program can produce a decision

# %%
class GetInfo():
    def __init__(self, stock):
        self.stock = stock
        try:
            # Attempt to fetch data
            self.Ticker = Ticker(stock)
        except ValueError as e: # TODO: do more error handling
            # Handle the error
            raise ValueError(f"Ticker does not exist. {e}")
        
    def current_price(self):
        try:
            current_price = self.Ticker.financial_data[self.stock]['currentPrice']
        except:
            try:
                current_price = self.Ticker.summary_detail[self.stock]['previousClose']
            except:
                current_price = float('nan')
        return current_price
    
    def free_cashflow(self):
        try:
            fcf = self.Ticker.cash_flow(trailing=False)['FreeCashFlow'].iloc[-1]
        except:
            fcf = float('nan')
        return fcf
    
    def shares_outstanding(self):
        try:
            shares_outstanding = self.Ticker.key_stats[self.stock]['sharesOutstanding']
        except:
            shares_outstanding = float('nan')
        return shares_outstanding
    
    def peratio(self):
        try:
            peratio = self.Ticker.valuation_measures['ForwardPeRatio'].mean() # forward P/E for the stock
        except:
            peratio = float('nan')
        return peratio
    
    def beta(self):
        try:
            beta = self.Ticker.key_stats[self.stock]['beta']
        except:
            beta = float('nan')
        return beta
    
    def sector(self):
        try:
            sector = str(self.Ticker.asset_profile[self.stock]['sector'])
        except:
            sector = 'undefined'
        if sector not in WACC_RATES:
            WACC_RATES[sector] = DEFAULT_WACC_RATE
        if sector not in AVGPERATIOS:
            AVGPERATIOS[sector] = DEFAULT_PE_RATIO
        return sector
    
    def marketcap(self):
        try:
            marketcap = self.Ticker.price[self.stock]['marketCap']
        except:
            marketcap = float('nan')
        return marketcap
    
    def marketcap_type(self, marketcap):
        if marketcap >= 10000000000:
            return 'largecap'
        if marketcap < 10000000000 and marketcap >= 2000000000:
            return 'midcap'
        if marketcap < 2000000000:
            return 'smallcap'
        if math.isnan(marketcap):
            return 'undefined'
        
    def dividend_yield(self):
        try:
            dividend_yield = self.Ticker.summary_detail[self.stock]['dividendYield']
        except:
            dividend_yield = float('nan')
        return dividend_yield
    
    """
    Returns the longest available history of dividends by year (as far back as 2014-01-01)
    If dividend history doesn't exist, returns None
    """
    def dividend_history(self):
        for start_date in STARTDATE_LIST:
            try:
                dividend = self.Ticker.dividend_history(start = start_date)
                if dividend.shape[0] != 0:
                    dividend_history = dividend['dividends']
                    dividend_history = pd.DataFrame(dividend_history.items(), columns=['date', 'dividends'])
                    dividend_history = dividend_history.explode('date').reset_index(drop=True)
                    dividend_history = dividend_history[dividend_history['date'] != self.stock]
                    dividend_history = dividend_history.reset_index(drop=True)

                    # Convert 'date' column to datetime
                    dividend_history['date'] = pd.to_datetime(dividend_history['date'])
                    # Group by year and sum up dividends
                    dividend_history = dividend_history.groupby(dividend_history['date'].dt.year)['dividends'].sum()
                    dividend_history = dividend_history.drop(dividend_history.index[-1])
                    dividend_history = dividend_history.rename_axis('year').reset_index(name='dividends')
                    return dividend_history['dividends']
            except Exception as e:
                pass
        return []

    """
    Returns the longest available history of price by interval specified (as far back as 2014-01-01)
    If price history doesn't exist, returns None
    """
    def price_history(self, interval):
        for start_date in STARTDATE_LIST:
            try:
                price_history = np.array(self.Ticker.history(start=start_date, interval=interval)['close'])
                if price_history.size != 0:
                    return price_history
            except Exception as e:
                pass
        return []
        
    
    """
    Returns dictionary with all esg scores info and peer esg scores info (dictionary with min, avg, max)
    Returns None if any of the information cannot be accessed
    """
    def esg_scores(self):
        try:
            esg_score_dict = self.Ticker.esg_scores[self.stock]
        except:
            esg_score_dict = None
        return esg_score_dict


# %% [markdown]
# ## class Analysis
# This class defines all the necessary analysis models for income and growth analyses
# - predict_growth
# 
#     This function creates a linear regression model using the scikit-learn library, and predicts the value for future time points, given a sequence of data from past time points.
# - compare_predictions
#     
#     This function compares two sequences of data and returns at how many time points the first sequence is greater than the second. 
#     
#     It is used to compare the predicted dividend yields for a stock against the S&P500 ETF.
# 
# - predict_fiveyr_price
# 
#     This function retrieves the history of stock prices and calls the predict_growth function to return a prediction of stock prices for the next 5 years.
# 
# - predict_fiveyr_dividend
# 
#     This function retrieves the history of dividends and calls the predict_growth function to return a prediction of dividends for the next 5 years.
# 
# - calculate_dcf_intrinsic_value
# 
#     This function calculates the intrinsic value of a stock, based on a DCF analysis. It retrieves data on free cash flow and calculates the discounted cash flow based on the wacc rates. Ref: https://www.investopedia.com/terms/i/intrinsicvalue.asp 
# 
# - calculate_upside
# 
#     This function calculates a stock's upside, given the intrinsic value.

# %%
class Analysis():
    def __init__(self, stock):
        self.stock = stock
        self.info = GetInfo(stock)
        self.sector = self.info.sector()
        self.current_price = self.info.current_price()

    # FOR GROWTH AND INCOME
    def predict_growth(self, data, time_points):
        X = np.arange(len(data)).reshape(-1, 1)
        y = data

        # Create and fit the linear regression model
        model = LinearRegression()
        model.fit(X, y)

        # Predict growth for the next time points
        future_time_points = np.arange(len(data), len(data) + time_points).reshape(-1, 1)
        predicted_growth = model.predict(future_time_points)

        return list(predicted_growth)
    
    def compare_predictions(self, stock_preds, sp_preds):
        stock = 0
        nan_count = 0
        total = len(stock_preds)
        for i in range(total):
            stock_pred= stock_preds[i]
            sp_pred = sp_preds[i]
            if (not math.isnan(stock_pred)) and (not math.isnan(sp_pred)):
                if stock_pred >= sp_pred:
                    stock += 1
            else:
                nan_count += 1
        if nan_count == total:
            return float('nan')
        return stock
    
    def predict_fiveyr_price(self):
        # Set pred num to 60 because we want to predict 5 years (60months) ahead
        price_history = self.info.price_history('1mo')
        if len(price_history) == 0:
            return []
        price_pred_fiveyrs = []
        price_pred = self.predict_growth(price_history, 60)
        index_list = [11, 23, 35, 47, 59]
        for index in index_list:
            price_pred_fiveyrs.append(price_pred[index])
        return price_pred_fiveyrs
    
    # FOR INCOME
    def predict_fiveyr_dividend(self):
        dividend_history = self.info.dividend_history()
        if len(dividend_history) == 0:
            return []
        return self.predict_growth(dividend_history, 5)

    # FOR GROWTH
    def calculate_dcf_intrinsic_value(self):
        # Assuming constant growth rate for simplicity
        growth_rate = GROWTH_RATE 
        # Discount rate
        discount_rate = WACC_RATES[self.sector]  
        # Get last year free cash flow
        fcf = self.info.free_cashflow()
        # Get the number of shares outstanding
        shares_outstanding = self.info.shares_outstanding()
        # Calculate terminal value using perpetual growth formula
        terminal_value = (fcf * (1 + growth_rate)) / (discount_rate - growth_rate)
        # Discount each year's cash flow
        discounted_cash_flows = [fcf / (1 + discount_rate) ** i for i in range(1, 6)]  # Discounting cash flows for 5 years
        # Add terminal value
        discounted_cash_flows.append(terminal_value / (1 + discount_rate) ** 5)
        # Calculate intrinsic value
        intrinsic_value = np.sum(discounted_cash_flows) / shares_outstanding

        return intrinsic_value
    
    def calculate_upside(self, intrinsic_value):
        return intrinsic_value/self.current_price - 1

# %% [markdown]
# ## class Decisions
# This class returns a decision or explanation for a given stock and client type
# - income
# 
#     The income analysis considers three metrics: predicted dividend yield, beta, and principle protection
# 
#     - Predicted dividend yield is derived through the predicted dividends and stock prices through linear regression, and is set to True if it outperforms the predicted dividend yield of S&P500 for more than 2 of the next 5 years.
# 
#     - Beta is obtained from yahooquery, and is set to True if it is less than or equal to 1.
# 
#     - Principle protection is derived as the sum of predicted stock price delta between now and 5 years from now and sum of predicted dividends over the next 5 years. It is set to True if it is above or equal to 0 (net gain). 
# 
#     - Given these 3 metrics, the analysis returns a decision based on the income decision table (description for decision is in global variables section).
# - growth
# 
#     The growth analysis considers three metrics: P/E ratio, upside, and predicted stock price growth
# 
#     - P/E ratio is obtained from yahooquery, and is set to True if it is greater than or equal to the average P/E ratio of the sector / market cap group the stock is in.
# 
#     - Upside is calculated through a DCF analysis of intrinsic value, and is set to True if it is greater than or equal to the average upside of the sector / market cap group the stock is in.
# 
#     - For both P/E ratio and upside, we compare it to the average of the sector / market cap group the stock is in, since they tend to vary a lot between sectors and market caps, and using the same threshold for all stocks will favor some sectors or market caps over others and hinder portfolio diversification.
# 
#     - Predicted stock price growth is derived through the predicted stock prices through linear regression, and is set to True if the 5 year growth rate outperforms the predicted stock price growth of S&P500.
# 
#     - Given these 3 metrics, the analysis returns a decision based on the growth decision table (description for decision is in global variables section).
# - default
#     
#     The default analysis makes a decision based on the combination of decisions that the income analysis and growth analysis returns.
#     Given these 2 decisions, the analysis returns a decision based on the default decision table (description for decision is in global variables section).
# - esg
# 
#     The esg analysis considers the ESG risk score and defaut analysis decison to make a decision.
#     The ESG risk score is obtained from yahooquery, and is set to True if it is smaller than or equal to the average ESG risk score of its peers.
#     Given the 2 metrics, the analysis returns a decision based on the ESG decision table (description for decision is in global variables section).
# - get_explanation
# 
#     Returns the descriptions of the metrics and decision processes that led to the decision.
# 

# %%
class TypeAnalysis():
    def __init__(self, stock):
        self.stock = stock
        self.info = GetInfo(self.stock)
        self.strategy = Analysis(self.stock)
        self.beta = self.info.beta()
        self.sector = self.info.sector()
        self.marketcap = self.info.marketcap()
        self.current_price = self.info.current_price()
        self.marketcap_type = self.info.marketcap_type(self.marketcap)


        # Predict stock price for next 5 years
        # Set pred num to 60 because we want to predict 5 years (60months) ahead
        self.price_pred_fiveyrs = self.strategy.predict_fiveyr_price()
        
        # Predict stock price for next 5 years
        self.fiveyr_delta = self.price_pred_fiveyrs[-1] - self.current_price
        self.fiveyr_delta_rate = (self.price_pred_fiveyrs[-1] - self.current_price) / self.current_price

        # For growth
        self.peratio = None
        self.sector_peratio_average = None
        self.upside = None
        self.intrinsic_value = None
        self.sector_upside_average = None
        self.intrinsic_value = self.strategy.calculate_dcf_intrinsic_value()
        self.upside = self.strategy.calculate_upside(self.intrinsic_value)
        self.peratio = self.info.peratio()
        if self.marketcap_type != 'undefined':
            self.sector_peratio_average = AVGPERATIOS[self.sector][self.marketcap_type]
            self.sector_upside_average = AVGUPSIDES[self.sector][self.marketcap_type]

        # For income
        self.income_decision = None
        self.dividend_pred_fiveyrs = None
        self.dividend_yield_pred_fiveyrs = None
        self.dividend_history = self.info.dividend_history()

        # For ESG
        self.esg_risk_score = None
        self.peer_esg_risk_score = None


    """
    List is [sector, explanation, beta, average dividend_yield_pred_fiveyrs, upside_ratio, peratio_ratio, fiveyr_delta_rate]
    """
    def default(self, income, growth):
        # The default strategy combines the income and growth metrics to make a decision
        # Add to list if the stock is good both for income and growth
        default = [self.sector, self.get_explanation('default')]
        default.append(income)
        default.append(growth)
        DEFAULT_DICT[self.stock] = default
        return

    """
    List is [sector, explanation, beta, average dividend_yield_pred_fiveyrs]
    """
    def income(self):
        # do not include in list if dividend has never been payed
        if len(self.dividend_history) != 0 and not math.isnan(self.beta):
            # Predict dividend for next 5 years
            self.dividend_pred_fiveyrs = self.strategy.predict_growth(self.dividend_history, 5)
            # Perform element-wise division to calculate dividend yield for next 5 years
            self.dividend_yield_pred_fiveyrs = [a / b for a, b in zip(self.dividend_pred_fiveyrs, self.price_pred_fiveyrs)]
            avg_dividend_yield = sum(self.dividend_yield_pred_fiveyrs)/5
            # If principle_protection is not achieved, don't include in list
            if self.fiveyr_delta + sum(self.dividend_pred_fiveyrs) >= 0 and not math.isnan(avg_dividend_yield):
                # Store the beta, and average of dividend_yield_pred_fiveyrs (sort by them later)
                INCOME_DICT[self.stock] = [self.sector, self.get_explanation('income'), self.beta, avg_dividend_yield]
                return [self.beta, avg_dividend_yield]
            
        return None
    
    """
    List is [sector, explanation, upside_ratio, peratio_ratio, fiveyr_delta_rate]
    """
    def growth(self):
        # If peratio is undefined, do not include in the list
        if not math.isnan(self.peratio) and not math.isnan(self.upside) and not math.isnan(self.fiveyr_delta_rate):
            # Calculate ratio of upside and peratio compared to the sector average
            upside_ratio = self.upside/self.sector_upside_average
            peratio_ratio = self.peratio/self.sector_peratio_average
            # Only include in list if all aspects are desirable
            if upside_ratio > 1 and peratio_ratio > 1:
                GROWTH_DICT[self.stock] = [self.sector, self.get_explanation('growth'), upside_ratio, peratio_ratio, self.fiveyr_delta_rate]
                return [upside_ratio, peratio_ratio, self.fiveyr_delta_rate]

        return None
    
    
    """
    List is [sector, explanation, esgscore_ratio]
    """
    def esg(self):
        esg_risk_scores = self.info.esg_scores()
        # if self.default() != None:
        # Do not include in the list if there is no ESG score or if it is not a good default stock
        if esg_risk_scores != None and not isinstance(esg_risk_scores, str):

            self.esg_risk_score = esg_risk_scores['totalEsg']
            self.peer_esg_risk_score = esg_risk_scores['peerEsgScorePerformance']['avg']

            # Calculate the ESG score ratio to peers
            # Smaller is better
            esgscore_ratio =  self.esg_risk_score/self.peer_esg_risk_score

            if esgscore_ratio < 1:
                ESG_DICT[self.stock] = [self.sector, self.get_explanation('esg'), esgscore_ratio]
            
        return 0
    
    def get_explanation(self, type):
        match type:
            case 'income':
                explanation = self.income_explanation()
                
            case 'growth':
                explanation = self.growth_explanation()
   
            case 'esg':
                explanation = self.esg_explanation()

            case 'default':
                explanation = self.default_explanation()
        
        return explanation
    
        
    def income_explanation(self):
        explanation = f"""
        {self.stock}: {self.sector} sector
        {self.stock} is suitable for an income portfolio, since 
        1) We project the stock to achieve principle protection over the next 5 years
        2) It has relatively high dividend yield, as we project its dividend yields as {["{:.4f}".format(num) for num in self.dividend_yield_pred_fiveyrs]} over the next 5 years
        3) It has a low volatility, with the beta being {self.beta}
        """
        return explanation

    def growth_explanation(self):
        explanation = f"""
        {self.stock}: {self.sector} sector
        {self.stock} is suitable for a growth portfolio, since 
        1) It has Forward Price-to-Earnings (P/E) ratio of {self.peratio}, which outperforms the sector average, which is {self.sector_peratio_average}
        2) The upside of the stock, calculated through a DCF Analysis of intrinsic value, is {self.upside}, which outperforms the sector average, which is {self.sector_upside_average}
        3) Based on linear regression on historical stock prices, we project the stock to have predicted growth rate of {self.fiveyr_delta_rate:.2f} 
        """
        return explanation
    
    # 1) It has a desirable Forward Price-to-Earnings (P/E) ratio of {self.peratio}, when the sector average is {self.sector_peratio_average}
    #     2) The upside of the stock, calculated through a DCF Analysis of intrinsic value, is desirable at {self.upside}, when the sector average is {self.sector_upside_average}
    #     3) Based on linear regression on historical stock prices, we project the stock to have predicted growth rate of {self.fiveyr_delta_rate:.2f} 

    def default_explanation(self):
        explanation = f"""
        {self.stock}: {self.sector} sector
        {self.stock} is suitable for an default portfolio, since we project it to perform well in terms of income and growth
        Positive indications for income:
        1) We project the stock to achieve principle protection over the next 5 years
        2) It has relatively high dividend yield, as we project its dividend yields as {["{:.4f}".format(num) for num in self.dividend_yield_pred_fiveyrs]} over the next 5 years
        3) It has a low volatility, with the beta being {self.beta}
        Positive indications for growth:
        1) It has Forward Price-to-Earnings (P/E) ratio of {self.peratio}, which outperforms the sector average, which is {self.sector_peratio_average}
        2) The upside of the stock, calculated through a DCF Analysis of intrinsic value, is {self.upside}, which outperforms the sector average, which is {self.sector_upside_average}
        3) Based on linear regression on historical stock prices, we project the stock to have predicted growth rate of {self.fiveyr_delta_rate:.2f} 
        """
        return explanation
    
    def esg_explanation(self):
        explanation = f"""
        {self.stock}: {self.sector} sector
        {self.stock} is suitable for an ESG portfolio, since it has an ESG risk score of {self.esg_risk_score}, which outperforms its peers, which has an average ESG risk score of {self.peer_esg_risk_score}, and performs well in terms of both income and growth
        Positive indications for income:
        1) We project the stock to achieve principle protection over the next 5 years
        2) It has relatively high dividend yield, as we project its dividend yields as {["{:.4f}".format(num) for num in self.dividend_yield_pred_fiveyrs]} over the next 5 years
        3) It has a low volatility, with the beta being {self.beta}
        Positive indications for growth:
        1) It has Forward Price-to-Earnings (P/E) ratio of {self.peratio}, which outperforms the sector average, which is {self.sector_peratio_average}
        2) The upside of the stock, calculated through a DCF Analysis of intrinsic value, is {self.upside}, which outperforms the sector average, which is {self.sector_upside_average}
        3) Based on linear regression on historical stock prices, we project the stock to have predicted growth rate of {self.fiveyr_delta_rate:.2f} 
        """
        return explanation

# %%
def analyze_stocks():
    for index, stock in enumerate(SP_LIST):
        analyzer = TypeAnalysis(stock)
        income = analyzer.income()
        growth = analyzer.growth()
        if income != None and growth != None:
            analyzer.default(income, growth)
            analyzer.esg()
        print(index+1)

def rank_income():
    # Rank by beta
    beta_ranking = dict(sorted(INCOME_DICT.items(), key=lambda x: x[1][2]))
    beta_rank_dict = {}
    for index, stock in enumerate(beta_ranking, start=1):
        beta_rank_dict[stock] = index

    # Rank by dividend yield
    dividend_yield_ranking = dict(sorted(INCOME_DICT.items(), key=lambda x: x[1][3]), reverse=True) 
    dividend_yield_rank_dict = {}
    for index, stock in enumerate(dividend_yield_ranking, start=1):
        dividend_yield_rank_dict[stock] = index

    for stock in INCOME_DICT:
        INCOME_RANKING[stock] = beta_rank_dict[stock] + dividend_yield_rank_dict[stock]

    # Smaller rank the better

def rank_growth():
    # Rank by upside
    upside_ranking = dict(sorted(GROWTH_DICT.items(), key=lambda x: x[1][2]), reverse=True)
    upside_rank_dict  = {}
    for index, stock in enumerate(upside_ranking, start=1):
        upside_rank_dict[stock] = index

    # Rank by forward pe ratio
    pe_ranking = dict(sorted(GROWTH_DICT.items(), key=lambda x: x[1][3]), reverse=True)
    pe_rank_dict   = {}
    for index, stock in enumerate(pe_ranking, start=1):
        pe_rank_dict[stock] = index

    # Rank by projected return
    projected_return_ranking = dict(sorted(GROWTH_DICT.items(), key=lambda x: x[1][4]), reverse=True) 
    projected_return_rank_dict  = {}
    for index, stock in enumerate(projected_return_ranking, start=1):
        projected_return_rank_dict[stock] = index

    for stock in GROWTH_DICT:
        GROWTH_RANKING[stock] = upside_rank_dict[stock] + pe_rank_dict[stock] + projected_return_rank_dict[stock]

    # Smaller rank the better

def rank_default():
    for stock in DEFAULT_DICT:
        DEFAULT_RANKING[stock] = INCOME_RANKING[stock] + GROWTH_RANKING[stock]
        # Smaller rank the better

def rank_esg():
    # Extract entries from ESG_DICT if the key is present in DEFAULT_RANKING
    esg_ranking = dict(sorted(ESG_DICT.items(), key=lambda x: x[1][2]))

    
    esg_rank_dict = {}
    for index, stock in enumerate(esg_ranking, start=1):
        esg_rank_dict[stock] = index

    for stock in esg_rank_dict:
        ESG_RANKING[stock] = esg_rank_dict[stock]
        # Smaller rank the better

def create_ranked_lists():
    rank_income()
    rank_growth()
    rank_default()
    rank_esg()
    # Sort the ranking and create list (and dict)
    with open("output1.txt", "a") as file:
        sorted_income_ranking = sorted(INCOME_RANKING.items(), key=lambda x: x[1])
        INCOME_RANKING_LIST = [item[0] for item in sorted_income_ranking]
        json_dict["INCOME_LIST"] = INCOME_RANKING_LIST

        sorted_growth_ranking = sorted(GROWTH_RANKING.items(), key=lambda x: x[1])
        GROWTH_RANKING_LIST = [item[0] for item in sorted_growth_ranking]
        json_dict["GROWTH_LIST"] = GROWTH_RANKING_LIST

        sorted_default_ranking = sorted(DEFAULT_RANKING.items(), key=lambda x: x[1])
        DEFAULT_RANKING_LIST = [item[0] for item in sorted_default_ranking]
        json_dict["DEFAULT_LIST"] = DEFAULT_RANKING_LIST

        sorted_esg_ranking = sorted(ESG_RANKING.items(), key=lambda x: x[1])
        ESG_RANKING_LIST = [item[0] for item in sorted_esg_ranking]
        json_dict["ESG_LIST"] = ESG_RANKING_LIST
        
    return

# %%
analyze_stocks()

# %%
create_ranked_lists()

# %%

json_dict["INCOME_DICT"] = INCOME_DICT
json_dict["GROWTH_DICT"] = GROWTH_DICT
json_dict["DEFAULT_DICT"] = DEFAULT_DICT
json_dict["ESG_DICT"] = ESG_DICT

with open(OUTPUT_FILE, 'w') as file:
    json.dump(json_dict, file)

# %%
# # To create the stock to sector dictionary
# for stock in SP_LIST:
#     STOCK_SECTOR_DICT[stock] = str(Ticker(stock).asset_profile[stock]['sector'])

# %% [markdown]
# # Appendix
# Recommended not to run due to long run time (~ 1 hour/appendix)

# %% [markdown]
# ## Appendix A
# Code to obtain 'AVGPERATIOS'

# %%
# # AVGPERATIOS = {'Technology': {'largecap': [], 'midcap': [], 'smallcap': []}, 'Healthcare': {'largecap': [], 'midcap': [], 'smallcap': []}, 'Financial Services': {'largecap': [], 'midcap': [], 'smallcap': []}, 'Consumer Cyclical': {'largecap': [], 'midcap': [], 'smallcap': []}, 'Consumer Defensive': {'largecap': [], 'midcap': [], 'smallcap': []}, 'Industrials': {'largecap': [], 'midcap': [], 'smallcap': []}, 'Energy': {'largecap': [], 'midcap': [], 'smallcap': []}, 'Utilities': {'largecap': [], 'midcap': [], 'smallcap': []}, 'Basic Materials': {'largecap': [], 'midcap': [], 'smallcap': []}, 'Real Estate': {'largecap': [], 'midcap': [], 'smallcap': []}, 'Communication Services': {'largecap': [], 'midcap': [], 'smallcap': []}}

# default_pe_ratio = float('nan')

# # Obtain P/E ratios for all stocks in S&P500
# for ticker in SP_LIST:
#     info = GetInfo(ticker)
#     sector = info.sector()
#     marketcap = info.marketcap_type(info.marketcap())
#     peratio = info.peratio()
#     AVGPERATIOS[sector][marketcap].append(peratio)

# # Calculate the average peratios for each sector and capsize
# for sector in SECTORS:
#     for marketcap in MARKETCAPS:
#         # Remove all 'nan' values
#         peratios = [x for x in AVGPERATIOS[sector][marketcap] if str(x) != 'nan']
#         # If insufficient data from S&P500 stocks, use default value
#         if len(peratios) != 0:
#             AVGPERATIOS[sector][marketcap] = sum(peratios)/len(peratios)
#         else:
#             AVGPERATIOS[sector][marketcap] = default_pe_ratio

# %% [markdown]
# ## Appendix B
# Code to obtain 'AVGUPSIDES'

# %%
# # AVGUPSIDES = {'Technology': {'largecap': [], 'midcap': [], 'smallcap': []}, 'Healthcare': {'largecap': [], 'midcap': [], 'smallcap': []}, 'Financial Services': {'largecap': [], 'midcap': [], 'smallcap': []}, 'Consumer Cyclical': {'largecap': [], 'midcap': [], 'smallcap': []}, 'Consumer Defensive': {'largecap': [], 'midcap': [], 'smallcap': []}, 'Industrials': {'largecap': [], 'midcap': [], 'smallcap': []}, 'Energy': {'largecap': [], 'midcap': [], 'smallcap': []}, 'Utilities': {'largecap': [], 'midcap': [], 'smallcap': []}, 'Basic Materials': {'largecap': [], 'midcap': [], 'smallcap': []}, 'Real Estate': {'largecap': [], 'midcap': [], 'smallcap': []}, 'Communication Services': {'largecap': [], 'midcap': [], 'smallcap': []}}

# default_upsides = float('nan')

# # Calculate the upside for all stocks in S&P500
# for ticker in SP_LIST:
#     info = GetInfo(ticker)
#     sector = info.sector()
#     marketcap = info.marketcap_type(info.marketcap())
#     strategy = Analysis(ticker)
#     upside = strategy.calculate_upside(strategy.calculate_dcf_intrinsic_value())
#     AVGUPSIDES[sector][marketcap].append(upside)

# # Calculate the average upside for each sector and capsize
# for sector in SECTORS:
#     for marketcap in MARKETCAPS:
#         # Remove all 'nan' values
#         upsides = [x for x in AVGUPSIDES[sector][marketcap] if str(x) != 'nan']
#         # If insufficient data from S&P500 stocks, use default value
#         if len(upsides) != 0:
#             AVGUPSIDES[sector][marketcap] = sum(upsides)/len(upsides)
#         else:
#             AVGUPSIDES[sector][marketcap] = default_upsides

# %% [markdown]
# 


