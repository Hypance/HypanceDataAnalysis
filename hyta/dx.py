import numpy as np
import pandas as pd
from hyta.atr import ATR


class DX:
    def __init__(
        self, high: pd.Series, low: pd.Series, close: pd.Series, period: int = 14
    ) -> None:
        self.high = high
        self.Low = low
        self.close = close
        self.period = period
        self.dx_data = pd.DataFrame(
            {"High": self.high, "Close": self.close, "Low": self.Low}
        )

    def TR(self) -> pd.Series:
        self.dx_data["TR"] = ATR(
            [self.dx_data["High"], self.dx_data["Low"], self.dx_data["Close"]],
            self.period,
        ).true_range()
        self.dx_data["TR"][0] = np.nan
        return self.dx_data["TR"]

    def plus_dm(self) -> pd.Series:
        first = [np.NAN]

        for i in range(1, len(self.Low)):
            low_diff = self.Low[i - 1] - self.dx_data["Low"][i]
            high_diff = self.dx_data["High"][i] - self.dx_data["High"][i - 1]

            if high_diff > low_diff:
                first.append(max(high_diff, 0))
            else:
                first.append(0)
        self.dx_data["+DM 1"] = pd.DataFrame({"+DM 1": first})
        return self.dx_data["+DM 1"]

    def minus_dm(self) -> pd.Series:
        first = [np.NAN]

        for i in range(1, len(self.dx_data["Low"])):
            low_diff = self.dx_data["Low"][i - 1] - self.dx_data["Low"][i]
            high_diff = self.dx_data["High"][i] - self.dx_data["High"][i - 1]

            if low_diff > high_diff:
                first.append(max(low_diff, 0))
            else:
                first.append(0)
        self.dx_data["-DM 1"] = pd.DataFrame({"-DM 1": first})
        return self.dx_data["-DM 1"]

    def smoothed_plus_dm14(self):
        self.plus_dm()
        first_14_plus_dm = self.dx_data["+DM 1"][: self.period + 1].sum()
        second_14_plus_dm = (
            first_14_plus_dm
            - (first_14_plus_dm / self.period)
            + self.dx_data["+DM 1"][self.period + 1]
        )

        new_dx_Data = np.array([])
        for i in range(self.period):
            new_dx_Data = np.append(new_dx_Data, np.nan)
        new_dx_Data = np.append(new_dx_Data, [first_14_plus_dm, second_14_plus_dm])

        for i in range(len(self.dx_data["+DM 1"]) - 16):
            other_14_plus_dm = (
                new_dx_Data[-1]
                - (new_dx_Data[-1] / self.period)
                + self.dx_data["+DM 1"][i + 16]
            )
            new_dx_Data = np.append(new_dx_Data, other_14_plus_dm)
            self.dx_data["+DM 14"] = pd.DataFrame({"+DM 14": new_dx_Data})
        return self.dx_data["+DM 14"]

    def smoothed_minus_dm14(self):
        self.minus_dm()
        first_14_minus_dm = self.dx_data["-DM 1"][: self.period + 1].sum()
        second_14_minus_dm = (
            first_14_minus_dm
            - (first_14_minus_dm / self.period)
            + self.dx_data["-DM 1"][self.period + 1]
        )

        new_dx_Data = np.array([])
        for i in range(self.period):
            new_dx_Data = np.append(new_dx_Data, np.nan)
        new_dx_Data = np.append(new_dx_Data, [first_14_minus_dm, second_14_minus_dm])

        for i in range(len(self.dx_data["-DM 1"]) - 16):
            other_14_minus_dm14 = (
                new_dx_Data[-1]
                - (new_dx_Data[-1] / self.period)
                + self.dx_data["-DM 1"][i + 16]
            )
            new_dx_Data = np.append(new_dx_Data, other_14_minus_dm14)
            self.dx_data["-DM 14"] = pd.DataFrame({"-DM 14": new_dx_Data})
        return self.dx_data["-DM 14"]

    def smoothed_tr14(self):
        self.TR()
        first_14_tr = self.dx_data["TR"][: self.period + 1].sum()
        second_14_tr = (
            first_14_tr
            - (first_14_tr / self.period)
            + self.dx_data["TR"][self.period + 1]
        )

        new_tr_Data = np.array([])
        for i in range(self.period):
            new_tr_Data = np.append(new_tr_Data, np.nan)
        new_tr_Data = np.append(new_tr_Data, [first_14_tr, second_14_tr])

        for i in range(len(self.dx_data["TR"]) - 16):
            other_14_tr = (
                new_tr_Data[-1]
                - (new_tr_Data[-1] / self.period)
                + self.dx_data["TR"][i + 16]
            )
            new_tr_Data = np.append(new_tr_Data, other_14_tr)
            self.dx_data["Smoothed TR"] = pd.DataFrame({"Smoothed TR": new_tr_Data})
        return self.dx_data["Smoothed TR"]

    def plus_di_14(self):
        self.smoothed_plus_dm14()
        self.smoothed_tr14()
        plus_di_14 = 100 * (self.dx_data["+DM 14"] / self.dx_data["Smoothed TR"])
        return plus_di_14

    def minus_di_14(self):
        self.smoothed_minus_dm14()
        self.smoothed_tr14()
        minus_di_14 = 100 * (self.dx_data["-DM 14"] / self.dx_data["Smoothed TR"])
        return minus_di_14

    def di_diff(self):
        self.plus_di_14()
        self.minus_di_14()
        di_difference = abs(self.plus_di_14() - self.minus_di_14())
        return di_difference

    def di_sum(self):
        self.plus_di_14()
        self.minus_di_14()
        di_sum = self.plus_di_14() + self.minus_di_14()
        return di_sum

    def dx(self):
        self.di_diff()
        self.di_sum()
        dx = abs(100 * (self.di_diff() / self.di_sum()))
        return dx
