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
           and previous closes when the current closes are less than previous closes.
           Then diveded to 14.
        """
        gain_list = []
        close = self.close
        for i in range(0, len(close)-1):
            if close[i+1] > close[i]:
                gain = round(close[i+1] - close[i],2)
                gain_list.append(gain)
            else:
                gain_list.append(0)
        gain_list = pd.Series(gain_list)
        gain_list = gain_list.rolling(self.period).sum()

        return gain_list / 14


    def loss_calculator(self) -> pd.Series:
        """
           From period, returns a pandas series
           by using loss_calculator function.
           Sum of the difference between the current closes
           and previous closes when the current closes are greater than previous closes.
           Then diveded to 14.
        """
        loss_list = []
        close = self.close
        for i in range(0, len(close) - 1):
            if close[i] > close[i + 1]:
                loss = round(close[i] - close[i + 1], 2)
                loss_list.append(loss)
            else:
                loss_list.append(0)
        loss_list = pd.Series(loss_list)
        loss_list = loss_list.rolling(self.period).sum()
        return loss_list / 14

    def rsi(self) -> pd.Series:
        """
            In this function, it calculates rs by using gain/loss
            and rsi by using 100-(100/(1+rs)).
            Returns a pandas series.
        """
        rs = self.gain_calculator()/self.loss_calculator()
        rsi = 100 - (100/(1+rs))
        return rsi