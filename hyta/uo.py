import numpy as np
import pandas as pd


class UO:
    """
    This class calculate UO for default 28-periods.

    It needs to get 'low','close' and 'high' values respectively.

    """

    def __init__(self, low, close, high) -> None:
        self.high = high
        self.low = low
        self.close = close

    def buyingPressure(self) -> np.ndarray:

        """
        This module, we calculate buying pressure with
        'buying pressure = close - min(low,PriorClose)'
        this equation.
        It needs to get close and low values.
        Returns the BuyingPressure array.
        Type of array is np.ndarray.
        """

        BP = []
        for i in range(0, len(self.close) - 1):
            bp = self.close[i + 1] - min(self.low[i + 1], self.close[i])
            BP.append(bp)
        return np.array(BP)

    def trueRange(self) -> np.ndarray:
        """
        This module, we calculate buying pressure with
        'true range = max(high,PriorClose) - min(low,PriorClose)'
        this equation.
        It needs to get high,close and low values.
        Returns the trueRange array.
        Type of array is np.ndarray.
        """
        TR = []
        for i in range(1, len(self.high)):
            tr = max(self.high[i], self.close[i - 1]) - min(
                self.low[i], self.close[i - 1]
            )
            TR.append(tr)
        return np.array(TR)

    def Average7(self) -> np.ndarray:
        """
        This module, we calculate 7-periods average with
        'A7 = (Sum of 7 period BP) / (Sum of 7 period TR)'
        this equation.
        It needs to get BP and TR values.
        Returns the A7 array.
        Type of array is np.ndarray.
        """
        cumulativeBP = np.cumsum(self.buyingPressure())
        cumulativeBP = np.insert(cumulativeBP, 0, 0)

        sevenPeriodedBP = [
            cumulativeBP[i] - cumulativeBP[i - 7] for i in range(7, len(cumulativeBP))
        ]

        cumulativeTR = np.cumsum(self.trueRange())
        cumulativeTR = np.insert(cumulativeTR, 0, 0)

        sevenPeriodedTR = [
            cumulativeTR[i] - cumulativeTR[i - 7] for i in range(7, len(cumulativeTR))
        ]

        A7 = np.array(sevenPeriodedBP) / np.array(sevenPeriodedTR)

        return A7

    def Average14(self) -> np.ndarray:
        """
        This module, we calculate 14-periods average with
        'A14 = (Sum of 14 period BP) / (Sum of 14 period TR)'
        this equation.
        It needs to get BP and TR values.
        Returns the A14 array.
        Type of array is np.ndarray.
        """
        cumulativeBP = np.cumsum(self.buyingPressure())
        cumulativeBP = np.insert(cumulativeBP, 0, 0)

        fourteenPeriodedBP = [
            cumulativeBP[i] - cumulativeBP[i - 14] for i in range(14, len(cumulativeBP))
        ]

        cumulativeTR = np.cumsum(self.trueRange())
        cumulativeTR = np.insert(cumulativeTR, 0, 0)

        fourteenPeriodedTR = [
            cumulativeTR[i] - cumulativeTR[i - 14] for i in range(14, len(cumulativeTR))
        ]

        A14 = np.array(fourteenPeriodedBP) / np.array(fourteenPeriodedTR)

        return A14

    def Average28(self) -> np.ndarray:
        """
        This module, we calculate 28-periods average with
        'A28 = (Sum of 28 period BP) / (Sum of 28 period TR)'
        this equation.
        It needs to get BP and TR values.
        Returns the A28 array.
        Type of array is np.ndarray.
        """
        cumulativeBP = np.cumsum(self.buyingPressure())
        cumulativeBP = np.insert(cumulativeBP, 0, 0)

        twentyeightPeriodedBP = [
            cumulativeBP[i] - cumulativeBP[i - 28] for i in range(28, len(cumulativeBP))
        ]

        cumulativeTR = np.cumsum(self.trueRange())
        cumulativeTR = np.insert(cumulativeTR, 0, 0)

        twentyeightPeriodedTR = [
            cumulativeTR[i] - cumulativeTR[i - 28] for i in range(28, len(cumulativeTR))
        ]

        A28 = np.array(twentyeightPeriodedBP) / np.array(twentyeightPeriodedTR)

        return A28

    def uo(self) -> pd.Series:
        """
        This module is final module.
        This calculates the UltimateOscillator for 28 periods.
        Needs to get A7,A14,A28 arrays.
        Returns ultOsc with type of pd.Series
        Due to not returns any NaN values, we use index slicing.
        """
        A7 = self.Average7()
        A14 = self.Average14()
        A28 = self.Average28()
        numerator = A7[21:] * 4 + A14[14:] * 2 + A28
        ultOsc = (numerator / 7) * 100
        return pd.Series(ultOsc)
