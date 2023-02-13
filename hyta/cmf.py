import pandas as pd


class CMF:

    """
    This class calculate the cmf for default 20-days period.
    ...
    Attributes
    ----------
    close : pandas.Series
    low   : pandas.Series
    high  : pandas.Series
    volume: pandas.Series
    period: pandas.Series

    Methods
    -------
    money_flow_multiplier(close,low,high):
        Returns the mfm.

    money_flow_volume(mfm, volume):
        Returns the mfv.

    cmf(money_flow_multiplier,money_flow_volume,data):
        Returns the cmf.

    """

    def __init__(
        self,
        close: pd.Series,
        low: pd.Series,
        high: pd.Series,
        volume: pd.Series,
        period: int = 20,
    ):
        self.close = close
        self.low = low
        self.high = high
        self.volume = volume
        self.period = period

    def money_flow_multiplier(self) -> pd.Series:
        mfm = ((self.close - self.low) - (self.high - self.close)) / (
            self.high - self.low
        )
        try:
            self.low / self.high
        except ZeroDivisionError as e:
            print("Value of high is zero:", e)

        return mfm

    def money_flow_volume(self) -> pd.Series:
        mfv = self.money_flow_multiplier() * self.volume
        return mfv

    def cmf(self) -> pd.Series:
        volume = self.volume
        period = self.period

        mfv = self.money_flow_volume()
        cmf = mfv.rolling(window=period).sum() / volume.rolling(window=period).sum()
        return cmf
