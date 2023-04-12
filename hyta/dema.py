from hyta.ema import EMA
import pandas as pd


class DEMA:
    """
    DEMA is a technical indicator that calculates the average
    price of an asset, giving more weight to recent prices.
    It's more responsive to price changes than a simple moving average,
    and is used by traders to identify buying and selling opportunities.
    """

    def __init__(self, close, period=9):
        self.period = period
        self.df = pd.DataFrame(data={"Close": close})
        self.close = self.df["Close"]

    def ema(self) -> pd.Series:
        """
        Calculating first EMA for DEMA
        """
        return EMA(self.close, self.period).calc_ema()

    def dema(self) -> pd.Series:
        """
        Calculating DEMA by using function --> 2*Ema - Ema of Ema
        """
        return (2 * self.ema()) - (EMA(self.ema(), self.period).calc_ema())
