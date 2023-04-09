import numpy as np
from numpy import nan as npNaN
import pandas as pd


class EMA:
    """
    This class calculates EMA according to user specified periods.
    If the user does not enter a value,the value is set to 9.

    Methods
    ---------
    sma(self):
        The EMA value cannot be calculated on the days before the period.
        In this function, NaN values are assigned to the days that cannot be calculated.
        The first day calculated is the SMA of the previous days.
    ---
    calc_ema(self):
        Calculates EMA values.
        EMA : (P * a) + (Previous EMA * (1 - a))
            P = Current Price
            a = Smoothing Factor = 2/(1+N)
            N = Period

        Returns pd.series.
    """

    def __init__(self, close: pd.Series, period: int = 9):
        self.close = close
        self.period = period

    def sma(self):
        self.close = self.close.copy()
        sma = self.close[0 : self.period].mean()
        self.close[: self.period - 1] = npNaN
        self.close.iloc[self.period - 1] = sma
        return self.close

    def calc_ema(self) -> pd.Series:
        df = pd.DataFrame()
        self.close = self.sma()
        df["EMA"] = self.close.ewm(span=self.period, adjust=False).mean()
        return df["EMA"]
