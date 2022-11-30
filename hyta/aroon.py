import pandas as pd

class Aroon():
    """
    This class calculate the aroon function for default 25-days period.
    To calculate this function It needs 'high' and 'low' values.
    """

    def __init__(self, period = 25) -> None:
        self.period = period
        self.df = pd.DataFrame(data = {"Adj Close": adj})


    """
    This method finds the highest data in the period and calculates how many periods 
    are there after that the highest data.
    """

    def __high_finder(self) -> pd.Series:
        df =  adj.rolling(self.period + 1).apply(lambda x: x.argmax())
        return (self.period - df +1)

    """
    This method finds the lowest data in the period and calculates how many periods 
    are there after that the lowest data.
    """

    def __low_finder(self):
        df =  adj.rolling(self.period + 1).apply(lambda x: x.argmin())
        return (self.period - df +1)

    """
    In this method , using by __high_finder(self): method and self.period It calculates
    aroon_up function by using 100*((25-self.__high_finder())/25)
    """

    def aroon_up(self) -> float:
        aroon_up = 100*((25-self.__high_finder())/25)
        return aroon_up

    """
        In this method , using by __low_finder(self): method and self.period It calculates
        aroon_down function 100*((25-self.__low_finder())/25)
    """

    def aroon_down(self) -> float:
        aroon_down = 100*((25-self.__low_finder())/25)
        return aroon_down

    """
    In this method, using aroon_up(self): and aroon_down(self): functions It calculates 
    aroon_oscilattor(self):
    """

    def aroon_oscilattor(self) -> float:
        return self.aroon_up() - self.aroon_down()


