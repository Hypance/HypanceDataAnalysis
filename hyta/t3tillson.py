from ema import EMA
import numpy as np
import pandas as pd


class t3Tillson:
    """
     This class calculates T3 Tillson Average indicator for period = 9.
     Attributes
     -----------
     close : pandas
     period : int
     a : 0.618
     c1 : -a**3
     c2 : 3*(a**2)+ 3*(a**3)
     c3 : -6(a**2) - 3*a - 3*(a**3)
     c4 : 1 + 3*a + a**3 + 3*(a**2)

     """

    def __init__(self, period: int = 9) -> None:
        self.period = period
        self.a = 0.618
        self.c1 = -self.a ** 3
        self.c2 = 3 * (self.a ** 2) + 3 * (self.a ** 3)
        self.c3 = -6*(self.a ** 2) - 3 * self.a - 3 * (self.a ** 3)
        self.c4 = 1 + 3 * self.a + self.a ** 3 + 3 * (self.a ** 2)
        self.df = pd.DataFrame(data={"Close": close})

    def ema1(self) -> pd.Series:
        """
        Calculates ema1 using cals_ema from EMA according to close and period.
        """
        e1 = EMA(self.close, self.period).calc_ema()
        return e1

    def ema2(self) -> pd.Series:
        """
        Calculates ema2 using cals_ema from EMA according to ema1 and period.
        """
        e2 = EMA(self.e1, self.period).calc_ema()
        return e2

    def ema3(self) -> pd.Series:
        """
        Calculates ema3 using cals_ema from EMA according to ema2 and period.
        """
        e3 = EMA(self.e2, self.period).calc_ema()
        return e3

    def ema4(self) -> pd.Series:
        """
        Calculates ema4 using cals_ema from EMA according to ema3 and period.
        """
        e4 = EMA(self.e3, self.period).calc_ema()
        return e4

    def ema5(self) -> pd.Series:
        """
        Calculates ema5 using cals_ema from EMA according to ema4 and period.
        """
        e5 = EMA(self.e4, self.period).calc_ema()
        return e5

    def ema6(self) -> pd.Series:
        """
        Calculates ema6 using cals_ema from EMA according to ema5 and period.
        """
        e6 = EMA(self.e5, self.period).calc_ema()
        return e6

    def T3(self) -> pd.Series:
        """
        Calculates T3 Tillson using the c1*e6 + c2*e5 + c3*e4 + c4*e3 formula
        """
        T3Tillson = self.c1 * self.e6 + self.c2 * self.e5 + self.c3 * self.e4 + self.c4 * (self.e3)
        return T3Tillson

data = pd.read_excel("/Users/esra/Library/Containers/com.microsoft.Excel/Data/Downloads/t3tillson.xlsx")
close = data["close"]

work = t3Tillson()
print(work.T3)