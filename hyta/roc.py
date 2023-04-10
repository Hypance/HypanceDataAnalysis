import numpy as np
import pandas as pd


class ROC:
    """
    This class calculate ROC for default 12-periods.
    It needs to get 'close' values respectively.
    """

    def __init__(self, close, period: int = 12) -> None:
        self.close = close
        self.period = period

    def roc(self) -> np.ndarray:
        """
        ROC = [(Close - Close n periods ago) / (Close n periods ago)] * 100
        Returns ROC array without nan values.
        """
        ROC = np.array([])
        for i in range(len(self.close) - self.period):
            ROC = np.append(
                ROC,
                ((self.close[i + self.period] - self.close[i]) / self.close[i]) * 100,
            )
        return pd.Series(ROC)
