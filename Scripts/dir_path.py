from enum import Enum

class DirPath(Enum):
    NEWS_BY_SOURCE = f"../Market Data and News/News/News by Source/"
    NEWS_BY_TICKER = f"../Market Data and News/News/News by Ticker/"

    BVB_FINANCIALS = f"../Market Data and News/Market Data/Financials/"
    BVB_FINANCIALS_FINANCIAL_CALENDAR = f"../Market Data and News/Market Data/Financials/Financial Calendar/"
    BVB_FINANCIALS_ANNUAL_FINANCIAL_INFORMATION = f"../Market Data and News/Market Data/Financials/Annual Financial Information/"

    BVB_TRADING = f"../Market Data and News/Market Data/Trading/"
    BVB_TRADING_PERFORMANCE = f"../Market Data and News/Market Data/Trading/Performance/"
    BVB_TRADING_HISTORY = f"../Market Data and News/Market Data/Trading/History/"

    BVB_OVERVIEW = f"../Market Data and News/Market Data/Overview/"
    BVB_MARKET_OVERIVIEW = f"../Market Data and News/Market Data/Overview/_Market Overview/"
    BVB_OVERVIEW_PRICES = f"../Market Data and News/Market Data/Overview/Prices/"
    BVB_OVERVIEW_INDICATORS = f"../Market Data and News/Market Data/Overview/Indicators/"
    BVB_OVERVIEW_ISSUE_INFO = f"../Market Data and News/Market Data/Overview/Issue Info/"

    TEST_FILES = f"../Test Files/"
    