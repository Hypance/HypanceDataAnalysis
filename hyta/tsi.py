import pandas as pd

class TSI:
    """
    Class to calculate True Strength Index
    """
    def __init__(self, close:list, long:int=25, short:int=13):
        self.close = close
        self.long = long
        self.short = short
    
    def calc_tsi(self) -> pd.Series :
        df = pd.DataFrame()
        df["close"] = self.close
        df["diff"] = self.close.diff(1)
        df["ema25"] = df["diff"].ewm(span=self.long, min_periods=self.long, adjust=False).mean()
        df["ema13"] = df["ema25"].ewm(span=self.short, min_periods=self.short, adjust=False).mean()
        df["abmo"] = abs(df["diff"])
        df["abmo25"] = df["abmo"].ewm(span=self.long, min_periods=self.long, adjust=False).mean()
        df["abmo13"] = df["abmo25"].ewm(span=self.short, min_periods=self.short, adjust=False).mean()
        df["TSI"] = df["ema13"]/df["abmo13"]*100
        return df["TSI"]

