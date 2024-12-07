import yfinance as yf

def get_data():

    AAPL = yf.download("AAPL", start="2010-01-01", end="2022-01-01")
    
    """ print()
    print(type(AAPL))
    print()
    print(AAPL.head())
    print()
    print(AAPL.shape)
    print()
    print(AAPL.columns)
    print()

    appl_close = AAPL["Close"]
    print (appl_close.head()) """

    print("Get data end function")

    return AAPL