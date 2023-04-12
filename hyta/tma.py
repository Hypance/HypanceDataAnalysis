import numpy as np
from hyta.movingaverage import MA


class TMA:
    """
    This class calculates TMA for default 20-days period.
    Attributes
    ---------------
    close : list
    period : int (optional, base=20)
    """

    def __init__(self, close, period: int = 20):
        self.period = period
        self.close = close

    """
    Calculating first MA for TMA.
    """

    def ma(self) -> np.ndarray:
        return MA(self.close, self.period).calcAverage()

    """
    Calculating the second MA which equals TMA.
    """

    def tma(self) -> np.ndarray:
        return MA(self.ma(), self.period).calcAverage()
