from hyta.ema import EMA
import numpy as np

class DEMA:

    def __init__(self, close, period=9):
        self.period = period - 1
        self.close = close

    """
    Calculating first EMA for DEMA
    """
    def ema(self) -> np.array:
        return EMA(self.close ,self.period).calc_ema()

    """
    Calculating dema by using function --> 2*Ema - Ema of Ema 
    """

    def dema(self) -> np.array:
        return (2 * EMA(self.close,self.period).calc_ema() ) - (EMA(EMA(self.close,self.period).calc_ema(),self.period).calc_ema())
