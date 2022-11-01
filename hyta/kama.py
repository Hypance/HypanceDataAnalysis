import numpy as np
import pandas as pd

class KAMA:
    """
    This class calculates Kaufman's Adaptive Moving Average.

    Methods
    --------------------
    change(self):
        Calculates the change needed to find efficiency ratio.
        change = abs(Close - Close(10 periods ago))
    -----
    volatility(self):
        Calculates the volatility needed to find efficiency ratio. 
        Volatility is the sum of the absolute value of the last ten price changes.

        volatility = sum10(abs(Close - Prior Close))
    -----
    efficiency_ratio(self):
        This method calculates efficiency ratio.
        The efficiency ratio shows the efficiency of price changes.

        ER = Change/Volatility
    -----
    smoothing_factor(self):
        The smoothing constant uses the ER and two smoothing constants
        based on an exponential moving average.

        SC = [ER * (fastest SC - slowest SC) + slowest SC] ** 2
    -----
    calc_kama(self):
        Calculates the KAMA values.

        CurrentKAMA = PriorKama + SC * (CurrentPrice - PriorKAMA)

        Returns pd.Series.
    """
    def __init__(self,close:pd.Series,period:int=10,fastest:int=2,slowest:int=30):
        self.close = close
        self.period = period
        self.fastest = fastest
        self.slowest = slowest

    def change(self):
        df["Change"] = abs(df["Close"].diff(periods = 10))
        return df["Change"]

    def volatility(self):
        df["Volatility"] = abs(df["Close"].diff(periods = 1))
        return df["Volatility"]

    def efficiency_ratio(self):
        self.change()
        self.volatility()
        df["ER"] = df["Change"] / df["Volatility"].rolling(window = self.period).sum()
        return df["ER"]

    def smoothing_constant(self):
        self.efficiency_ratio()
        df["sc"] = ((df["ER"] * (2 / (self.fastest+1) - 2 / (self.slowest+1))) + (2 / (self.slowest+1))) ** 2
        return df["sc"]

    def calc_kama(self):
        self.smoothing_constant()
        df["kama"] = pd.Series()
        
        for i in range(1,len(df["Close"])):
            df["kama"][:self.period - 1] = np.nan
            df["kama"].iloc[self.period - 1] = df["Close"].iloc[self.period - 1]

            if df["kama"][i] != np.nan :
                df["kama"][i] = df["kama"][i-1] + df["sc"][i] * (df["Close"][i] - df["kama"][i-1])              
        return df["kama"]