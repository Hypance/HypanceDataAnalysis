import pandas as pd


class CMF:

    """
    This class calculate the CMF (Chaikin Money Flow) for default 20-days period.
    ...
    Attributes
    ----------
    high : pandas.Series
        The high prices of a financial instrument for each period.
    low : pandas.Series
        The low prices of a financial instrument for each period.
    close : pandas.Series
        The closing prices of a financial instrument for each period.
    period : int, 20
        The number of periods to use for the ADX calculation. Default is 14.

    Methods
    -------
    money_flow_multiplier(self):
        Returns the mfm.

    money_flow_volume(self):
        Returns the mfv.

    cmf(self):
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
