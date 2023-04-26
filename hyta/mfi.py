import pandas as pd
import numpy as np


class MFI:
    """
    This class calculate the money flow index for default 14-days period .
    ...
    Attributes
    ----------
    close : pd.Series
    low : pd.Series
    high : pd.Series
    volume: pd.Series
    Methods
    -------
    typical_price(high,low,close):
        Returns the typical price.

    raw_money_flow(volume,typical_price):
        Returns the raw money flow.

    up_or_down(self):
        Returns 1.0 or -1.0 which in the list.

    one_period_positive_mf(self):
        Returns the positive money flow for 1-period.

    one_period_negative_mf(self):
        Returns the negative money flow for 1-period.

    positive_money_flow(period:int,data):
        Returns the positive money flow.

    negative_money_flow(period:int,data):
        Returns the negative money flow.

    money_ratio(positive_money_flow, negative_money_flow,period):
        Returns the money ratio.

    money_flow_index(money_ratio):
        Return the money flow index (mfi)
    """

    def __init__(
        self,
        close: pd.Series,
        low: pd.Series,
        high: pd.Series,
        volume: pd.Series,
        period: int = 14,
    ):
        self.close = close
        self.low = low
        self.high = high
        self.volume = volume
        self.period = period

    def typical_price(self) -> pd.Series:
        return (self.high + self.low + self.close) / 3

    def raw_money_flow(self) -> pd.Series:
        return self.volume * self.typical_price()[1:]

    def up_or_down(self) -> list:
        up_or_down = [np.nan]
        typical_price = self.typical_price()
        close_list = self.close.tolist()

        for i in range(len(close_list) - 1):
            if typical_price[i] < typical_price[i + 1]:
                up_or_down.append(1.0)
            else:
                up_or_down.append(-1.0)
        return up_or_down

    def one_period_positive_mf(self) -> pd.Series:
        up_or_down = self.up_or_down()
        one_period_positive_mf = [np.nan]
        raw_money_flow = self.raw_money_flow()
        for i in range(1, len(up_or_down)):
            if up_or_down[i] == np.nan:
                continue
            elif up_or_down[i] == 1.0:
                one_period_positive_mf.append(raw_money_flow[i])
            else:
                one_period_positive_mf.append(0)
        return pd.Series(one_period_positive_mf)

    def one_period_negative_mf(self) -> pd.Series:
        up_or_down = self.up_or_down()
        one_period_negative_mf = [np.nan]
        raw_money_flow = self.raw_money_flow()
        for i in range(1, len(up_or_down)):
            if up_or_down[i] == np.nan:
                continue
            elif up_or_down[i] == -1.0:
                one_period_negative_mf.append(raw_money_flow[i])
            else:
                one_period_negative_mf.append(0)
        return pd.Series(one_period_negative_mf)

    def positive_money_flow(self) -> pd.Series:
        positive_mf = self.one_period_positive_mf().rolling(window=self.period).sum()
        return positive_mf

    def negative_money_flow(self) -> pd.Series:
        negative_mf = self.one_period_negative_mf().rolling(window=self.period).sum()
        return negative_mf

    def money_ratio(self) -> pd.Series:
        return self.positive_money_flow() / self.negative_money_flow()

    def money_flow_index(self) -> pd.Series:
        mfi = 100 - (100 / (1 + self.money_ratio()))
        return mfi
