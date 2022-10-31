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

    """
    From period, returns a pandas series
    by using gain_calculator function.
    Sum of the difference between the current closes
    and previous closes when the current closes are less than previous closes.
    Then diveded to 14.
    """

    def gain_calculator(self) -> pd.Series:
        gain1 = []
        for i in range(0, len(close)-1):
            if close[i+1] > close[i]:
                gain = round(close[i+1] - close[i],2)
                gain1.append(gain)
            else:
                gain1.append(0)
        gain1 = pd.Series(gain1)
        gain1 = gain1.rolling(self.period).sum()
        return gain1 / 14

    """
    From period, returns a pandas series
    by using loss_calculator function.
    Sum of the difference between the current closes
    and previous closes when the current closes are greater than previous closes.
    Then diveded to 14.
    """

    def loss_calculator(self) -> pd.Series:
        loss1 = []
        for i in range(0, len(close) - 1):
            if close[i] > close[i + 1]:
                loss = round(close[i] - close[i + 1], 2)
                loss1.append(loss)
            else:
                loss1.append(0)
        loss1 = pd.Series(loss1)
        loss1 = loss1.rolling(self.period).sum()
        return loss1 / 14

    """
    In this function, it calculates rs by using gain/loss
    and rsi by using 100-(100/(1+rs)).
    Returns a pandas series.
    """

    def rsi(self) -> pd.Series:
        rs = self.gain_calculator()/self.loss_calculator()
        rsi = 100 - (100/(1+rs))
        return rsi

