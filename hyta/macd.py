import pandas as pd
import numpy as np


class MACD:

    """
    This class calculates MACD for default EMA1=12, EMA2=26 and SIGNAL=9.
    But you can give different input for all.

    Attributes
    ---------------
    close : list
    EMA1  : int
    EMA1  : int
    SIGNAL: int
    """

    def __init__(self, close, EMA1=12, EMA2=26, SIGNAL=9):
        self.close = close
        self.EMA1 = EMA1
        self.EMA2 = EMA2
        self.SIGNAL = SIGNAL

        # we only need the close data

    def Ema_1(self) -> list:

        Ema_first = [np.mean(self.close[: self.EMA1])]

        # Ema_12 is essential for the MACD, this "12" can be changable, but sorurces take "12".
        # For Ema_12 first we need to mean of first 12 days.
        # Other values of Ema_12 comes from the below calculation. Ema_12 values listed in "for" loop.
        for i in range(len(self.close) - self.EMA1):
            Ema_first.append(
                self.close[i + self.EMA1] * (2 / (self.EMA1 + 1))
                + (Ema_first[i] * (1 - (2 / (self.EMA1 + 1))))
            )

        return Ema_first

    def Ema_2(self) -> list:

        Ema_second = [np.mean(self.close[: self.EMA2])]

        # Ema_12 is essential for the MACD, this "12" can be changable, but sorurces take "12".
        # For Ema_12 first we need to mean of first 12 days.
        # Other values of Ema_12 comes from the below calculation. Ema_12 values listed in "for" loop.
        for i in range(len(self.close) - self.EMA2):
            Ema_second.append(
                self.close[i + self.EMA2] * (2 / (self.EMA2 + 1))
                + (Ema_second[i] * (1 - (2 / (self.EMA2 + 1))))
            )

        return Ema_second

    def MovingAverageConvergenceDivergence(self) -> list:

        # MACD values calculated with (Ema_12 - Ema_26).
        # Datas must be taken from the same day. Because of that i add "14" for Ema_12 values.
        macd = []
        for i in range(len(self.close) - self.EMA2 + 1):
            macd.append(self.Ema_1()[self.EMA2 - self.EMA1 + i] - self.Ema_2()[i])

        return macd

    def Signal(self) -> list:

        # For Signal values, first value is the mean of first 9 MACD values.
        # Other values of Signal comes from the below calculation.
        signal = [np.mean(self.MovingAverageConvergenceDivergence()[0 : self.SIGNAL])]
        for i in range(len(self.close) - self.EMA2 - self.SIGNAL + 1):
            signal.append(
                self.MovingAverageConvergenceDivergence()[i + self.SIGNAL]
                * (2 / (self.SIGNAL + 1))
                + (signal[i] * (1 - ((2 / (self.SIGNAL + 1)))))
            )

        return signal

    def Histogram(self) -> list:
        # Same day of MACD(starting from 8) and Signal values we calculate Histogram values with (MACD - Signal).
        histogram = []
        for i in range(len(self.close) - self.EMA2 - self.SIGNAL + 2):
            histogram.append(
                self.MovingAverageConvergenceDivergence()[self.SIGNAL - 1 + i]
                - self.Signal()[i]
            )
        return histogram

    def Result(self) -> pd.Series:

        d = {
            "Ema_first": pd.Series(
                self.Ema_1(),
                index=[i for i in range(0, len(self.close) - self.EMA1 + 1)],
            ),
            "Ema_second": pd.Series(
                self.Ema_2(),
                index=[
                    i
                    for i in range(
                        self.EMA2 - self.EMA1, len(self.close) - self.EMA1 + 1
                    )
                ],
            ),
            "Histogram": pd.Series(
                self.Histogram(),
                index=[
                    i
                    for i in range(
                        self.EMA2 - self.EMA1 + self.SIGNAL - 1,
                        len(self.close) - self.EMA1 + 1,
                    )
                ],
            ),
        }
        return d
