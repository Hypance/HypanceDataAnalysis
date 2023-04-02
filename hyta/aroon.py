import pandas as pd


class Aroon:
    """
    This class calculate the aroon function for default 25-days period.
     To calculate this function It needs adj close value.
    """

    def __init__(self, adj_close, period=25) -> None:
        self.period = period
        self.df = pd.DataFrame(data={"Adj Close": adj_close})

    def __high_finder(self) -> pd.Series:
        """
        This method finds the highest data in the period and calculates how many periods
        are there after that the highest data.
        """
        df = (
            self.df["Adj Close"]
            .rolling(self.period + 1)
            .apply(lambda x: x.argmax(), raw=True)
        )
        return (self.period - df + 1).squeeze()

    def __low_finder(self) -> pd.Series:
        """
        This method finds the lowest data in the period and calculates how many periods
        are there after that the lowest data.
        """
        df = (
            self.df["Adj Close"]
            .rolling(self.period + 1)
            .apply(lambda x: x.argmin(), raw=True)
        )
        return (self.period - df + 1).squeeze()

    def aroon_up(self) -> pd.Series:
        """
        In this method , using by __high_finder(self): method and self.period It calculates
        aroon_up function by using 100*((25-self.__high_finder())/25)
        """
        aroon_up = 100 * ((25 - self.__high_finder()) / 25)
        return aroon_up

    def aroon_down(self) -> pd.Series:
        """
         In this method , using by __low_finder(self): method and self.period It calculates
        aroon_down function 100*((25-self.__low_finder())/25)
        """
        aroon_down = 100 * ((25 - self.__low_finder()) / 25)
        return aroon_down

    def aroon_oscilattor(self) -> pd.Series:
        """
        In this method, using aroon_up(self): and aroon_down(self): functions It calculates
        aroon_oscilattor(self):
        """
        return self.aroon_up() - self.aroon_down()
