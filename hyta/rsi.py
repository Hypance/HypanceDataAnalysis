import pandas as pd


class RSI:
    """
    This class calculates RSI for period = 14.
    Attributes
    -----------
    close : pandas
    period : int
    """

    def __init__(self, close, period: int = 14) -> None:
        self.close = close
        self.period = period

    def gain_calculator(self) -> pd.Series:
        """
        From period, returns a pandas series
        by using gain_calculator function.
        Sum of the difference between the current closes
        and previous closes when the current closes
        are less than previous closes.
        Then diveded to 14.
        """
        close = self.close
        gain_list = pd.Series(0.0, index=close.index)
        for i in range(1, len(close)):
            if close[i] > close[i - 1]:
                gain = close[i] - close[i - 1]
                gain_list[i] = gain
        gain_avg = gain_list.rolling(window=self.period).mean()

        return gain_avg

    def loss_calculator(self) -> pd.Series:
        """
        From period, returns a pandas series
        by using loss_calculator function.
        Sum of the difference between the current closes
        and previous closes when the current closes
        are greater than previous closes.
        Then diveded to 14.
        """
        close = self.close
        loss_list = pd.Series(0.0, index=close.index)
        for i in range(1, len(close)):
            if close[i] < close[i - 1]:
                loss = close[i - 1] - close[i]
                loss_list[i] = loss
        loss_avg = loss_list.rolling(window=self.period).mean()

        return loss_avg

    def rsi(self) -> pd.Series:
        """
        In this function, it calculates rs by using gain/loss
        and rsi by using 100-(100/(1+rs)).
        Returns a pandas series.
        """
        gain = self.gain_calculator()
        loss = self.loss_calculator()
        rs = gain / loss
        rs[rs == float("inf")] = 0
        rsi = 100 - (100 / (1 + rs))
        return rsi
