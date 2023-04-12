import pandas as pd
import numpy as np
from hyta.dx import DX


class ADX:
    
    """
    A class used for calculating the ADX (Average Directional Index) of a given financial data set.    
    The default setting period is 14.

    The ADX is calculated using the directional movement index (DMI) lines, which are composed of the
    positive directional indicator (+DI) and the negative directional indicator (-DI). The ADX is derived
    from the relationship between the +DI and -DI lines and measures the strength of the trend on a scale of 0-100.
    A high ADX value indicates a strong trend, while a low ADX value suggests a weak or non-existent trend.

    Attributes
    ----------
    high : pandas.Series
        The high prices of a financial instrument for each period.
    low : pandas.Series
        The low prices of a financial instrument for each period.
    close : pandas.Series
        The closing prices of a financial instrument for each period.
    period : int, 14
        The number of periods to use for the ADX calculation. Default is 14.

    Methods
    -------
    adx(self):
        Returns the adx.
    """

    def __init__(self, high, low, close, period=14):
        self.data = pd.DataFrame({"high": high, "low": low, "close": close})
        self.period = period

    def adx(self):
        dx_data = DX(self.data["high"], self.data["low"], self.data["close"]).dx()
        dx_mean = dx_data[self.period : (self.period + 13)].mean()

        self.data["ADX"] = np.nan
        self.data["ADX"][27] = dx_mean
        other_value = []
        for i in range(28, len(dx_data) + 1):
            adx_result = (
                (self.data["ADX"][i - 1] * (self.period - 1)) + dx_data[i - 1]
            ) / self.period
            other_value.append(adx_result)
            self.data["ADX"][28:] = other_value[i - 28]

        return other_value[-1]