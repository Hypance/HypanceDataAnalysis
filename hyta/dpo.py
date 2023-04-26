import numpy as np
import pandas as pd


class DPO:
    # required input: dataset(array),period(int)
    def __init__(self, dataset: list, period: int = 4) -> None:
        self.dataset = dataset
        self.period = period

    def moving_average(self):  # Calculates the MA
        n = self.period  # for a period by using Index Slicers
        ret = np.cumsum(self.dataset)
        ret[n:] = ret[n:] - ret[:-n]
        return ret[n - 1 :] / n

    def closes(self):  # Getting (n/2)+1th close price
        n = self.period  # to calculate DPO
        tempArr = []
        for i in range(n - 2, ((n - 2) + 2 * len(self.moving_average())), 2):
            tempArr.append(self.dataset[(i // 2) + 1])
        periodCloses = np.array(tempArr)
        return periodCloses

    # Starting function, it returns a list.
    def dpo(self):
        dpoFinalize = np.subtract(self.closes(), self.moving_average())
        return pd.Series(dpoFinalize)
