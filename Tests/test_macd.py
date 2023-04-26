import unittest
import numpy as np
import pandas as pd
from hyta.macd import MACD


class TestMACD(unittest.TestCase):

    path = "Tests/files/MACD.xlsx"

    @classmethod
    def setUpClass(cls):
        cls.data = pd.read_excel(cls.path)
        cls.close = cls.data["Close"].to_list()
        cls.result_ema1 = cls.data["12 Day EMA"].to_list()
        cls.result_ema2 = cls.data["26 Day EMA"].to_list()
        cls.result_macd = cls.data["MACD"].to_list()
        cls.result_signal = cls.data["Signal"].to_list()
        cls.result_histogram = cls.data["Histogram"].to_list()

    @classmethod
    def tearDownClass(cls):
        del cls.data
        del cls.close
        del cls.result_ema1
        del cls.result_ema2
        del cls.result_macd
        del cls.result_signal
        del cls.result_histogram

    # below function is testing ema_1 results with respect to excel spreadsheet
    def test_ema1(self):
        self.result = MACD(self.close)
        ema_value1 = 12

        self.assertAlmostEqual(
            self.result_ema1[ema_value1 - 1], self.result.Ema_1()[0], 2
        )
        self.assertAlmostEqual(
            self.result_ema1[ema_value1 + 1], self.result.Ema_1()[2], 2
        )
        self.assertEqual(self.result_ema1[-1], self.result.Ema_1()[-1])

        self.assertEqual(
            len(self.result_ema1) - ema_value1 + 1, len(self.result.Ema_1())
        )

    # below function is testing ema_2 results with respect to excel spreadsheet
    def test_ema2(self):
        self.result = MACD(self.close)
        ema_value2 = 26

        self.assertAlmostEqual(
            self.result_ema2[ema_value2 - 1], self.result.Ema_2()[0], 2
        )
        self.assertAlmostEqual(
            self.result_ema2[ema_value2 + 1], self.result.Ema_2()[2], 2
        )
        self.assertEqual(self.result_ema2[-1], self.result.Ema_2()[-1])

        self.assertEqual(
            len(self.result_ema2) - ema_value2 + 1, len(self.result.Ema_2())
        )

    # below function is testing macd results with respect to excel spreadsheet
    def test_moving_average_convergence_divergence(self):
        self.result = MACD(self.close)
        ema_value2 = 26

        self.assertAlmostEqual(
            self.result_macd[ema_value2 + 1],
            self.result.MovingAverageConvergenceDivergence()[2],
            2,
        )
        self.assertAlmostEqual(
            self.result_macd[ema_value2 - 1],
            self.result.MovingAverageConvergenceDivergence()[0],
            2,
        )
        self.assertEqual(
            self.result_macd[-1], self.result.MovingAverageConvergenceDivergence()[-1]
        )

        self.assertEqual(
            len(self.result_macd) - ema_value2 + 1,
            len(self.result.MovingAverageConvergenceDivergence()),
        )

    # below function is testing signal results with respect to excel spreadsheet
    def test_signal(self):
        self.result = MACD(self.close)
        ema_value2 = 26
        signal_value = 9

        self.assertAlmostEqual(
            self.result_signal[ema_value2 + signal_value - 2],
            self.result.Signal()[0],
            2,
        )
        self.assertAlmostEqual(
            self.result_signal[ema_value2 + signal_value], self.result.Signal()[2], 2
        )
        self.assertEqual(self.result_signal[-1], self.result.Signal()[-1])

        self.assertEqual(
            len(self.result_signal) - ema_value2 - signal_value + 2,
            len(self.result.Signal()),
        )

    # below function is testing histogram results with respect to excel spreadsheet
    def test_histogram(self):
        self.result = MACD(self.close)
        ema_value2 = 26
        signal_value = 9

        self.assertAlmostEqual(
            self.result_histogram[ema_value2 + signal_value - 2],
            self.result.Histogram()[0],
            2,
        )
        self.assertAlmostEqual(
            self.result_histogram[ema_value2 + signal_value],
            self.result.Histogram()[2],
            2,
        )
        self.assertEqual(self.result_histogram[-1], self.result.Histogram()[-1])

        self.assertEqual(
            len(self.result_histogram) - ema_value2 - signal_value + 2,
            len(self.result.Histogram()),
        )

    # below function is testing corresponding ema_1 and ema_2 results
    def test_ema1_ema2_default(self):
        ema_1 = 12
        ema_2 = 26

        self.assertEqual(
            len(MACD(self.close).Ema_1()) - len(MACD(self.close).Ema_2()), ema_2 - ema_1
        )

    # below function is testing corresponding ema_1 and ema_2 results with different inputs
    def test_ema1_ema2_18_30(self):
        ema_1 = 18
        ema_2 = 30

        self.assertEqual(
            len(MACD(self.close, 18, 30).Ema_1())
            - len(MACD(self.close, 18, 30).Ema_2()),
            ema_2 - ema_1,
        )

    # below function is testing corresponding ema_2 and histogram results
    def test_ema2_histogram_default(self):
        ema_1 = 12
        ema_2 = 26
        signal = 9

        self.assertEqual(
            len(MACD(self.close).Ema_2()) - len(MACD(self.close).Histogram()),
            signal - 1,
        )

    # below function is testing corresponding ema_2 and histogram results with different inputs
    def test_ema2_histogram_18_30_12(self):
        ema_1 = 18
        ema_2 = 30
        signal = 12

        self.assertEqual(
            len(MACD(self.close, 18, 30, 12).Ema_2())
            - len(MACD(self.close, 18, 30, 12).Histogram()),
            signal - 1,
        )

    # Abnormal inputs will be checked prior to sending data to indicators
    # below functions is testing for different unusual inputs
    # def test_ema2_histogram_none(self):
    #     ema_1=0
    #     ema_2=0
    #     signal=0
    #     self.result_ema2=MACD(self.close,0,0,0).Ema_2()
    #     self.result_histogram=MACD(self.close,0,0,0).Histogram()

    #     self.assertEqual(len(self.result_ema2)-len(self.result_histogram),signal-1)
    #     np.testing.assert_equal(self.result_ema2[-1],np.nan)
    #     np.testing.assert_equal(self.result_histogram[-1],np.nan)


if __name__ == "__main__":
    unittest.main(argv=["first-arg-is-ignored"], exit=False)
