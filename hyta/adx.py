import pandas as pd
import numpy as np
from hyta.dx import DX


class ADX:
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