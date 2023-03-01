import pandas as pd
import numpy as np


class CCI:
    def __init__(self, high, low, close, period):
        self.df = pd.DataFrame(data={"high": high, "low": low, "close": close})
        self.period = period

    # typical_price as TP
    def TP(self) -> pd.Series:
        df = pd.DataFrame()
        df["TP"] = (self.df["high"] + self.df["low"] + self.df["close"]) / 3
        return df["TP"]

    # Simple_Moving_Average as SMA. It is calculated through TP.
    def SMA(self, tp: pd.Series) -> pd.Series:
        df = pd.DataFrame()
        df["TP"] = tp.values
        df["SMA"] = df["TP"].rolling(20).mean()
        return df["SMA"]

    # Mean_Deviation as MAD. It is calculated through TP.
    def MAD(self, tp: pd.Series) -> pd.Series:
        df = pd.DataFrame()
        df["TP"] = tp.values
        df["MAD"] = (
            df["TP"].rolling(20).apply(lambda x: np.mean(np.absolute(x - np.mean(x))))
        )
        return df["MAD"]

    # Commodity_Channel_Index as CCI
    def CCI(self):
        df = pd.DataFrame()
        df["TP"] = self.TP()
        df["SMA"] = self.SMA(df["TP"])
        df["MAD"] = self.MAD(df["TP"])
        df["CCI"] = (df["TP"] - df["SMA"]) / (0.015 * df["MAD"])
        return df["CCI"]
