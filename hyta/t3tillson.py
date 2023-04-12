from hyta.ema import EMA
import numpy as np
import pandas as pd


class t3Tillson:
    """
    Calculates the T3 Tillson indicator for a given set of closing prices.
    It uses six exponential moving averages
    calculated using the "EMA" class from the "ema" module.
    The class constructor takes a list or array of
    closing prices as "close" and an optional integer as "period" (default value is 9)
    that specifies the number of periods to use in the calculation.
    """

    def __init__(self, close, period: int = 9) -> None:
        self.period = period
        self.a = 0.618
        self.c1 = -self.a**3
        self.c2 = 3 * (self.a**2) + 3 * (self.a**3)
        self.c3 = -6 * (self.a**2) - 3 * self.a - 3 * (self.a**3)
        self.c4 = 1 + 3 * self.a + self.a**3 + 3 * (self.a**2)
        self.df = pd.DataFrame(data={"Close": close})
        self.close = self.df["Close"]
        self.e1 = self.ema1()
        self.e2 = self.ema2()
        self.e3 = self.ema3()
        self.e4 = self.ema4()
        self.e5 = self.ema5()
        self.e6 = self.ema6()

    def ema1(self) -> pd.Series:
        """
        Calculates ema1 using calc_ema from EMA according to close and period.
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
        T3Tillson = (
            self.c1 * self.e6
            + self.c2 * self.e5
            + self.c3 * self.e4
            + self.c4 * self.e3
        )
        return T3Tillson
