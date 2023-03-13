import unittest
import pandas as pd
from hyta.Stochastic_Oscillator import StochasticOscillator


class TestStochasticOscillator(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.path = "Tests/files/StochasticOscillator.xlsx"
        cls.data = pd.read_excel(cls.path)

    @classmethod
    def tearDownClass(cls):
        del cls.data

    def setUp(self) -> None:
        self.high = self.data["High"]
        self.low = self.data["Low"]
        self.close = self.data["Close"]
        self.StochasticOscillator_data = StochasticOscillator(
            self.high, self.low, self.close
        )
        self.so = StochasticOscillator(
            self.data["High"], self.data["Low"], self.data["Close"], periods=5
        )

    def tearDown(self):
        del self.so

    def test_fast_stochastic(self):
        self.assertAlmostEqual(
            self.so.fast_stochastic()[10], self.data["fast_stochastic"][10]
        )
        self.assertGreater(self.so.fast_stochastic()[15], -1)
        self.assertLess(self.so.fast_stochastic()[35], 99)

    def test_slow_stochastic(self):
        self.assertAlmostEqual(
            self.so.slow_stochastic()[9], self.data["slow_stochastic"][9]
        )
        self.assertGreater(self.so.slow_stochastic()[15], -1)
        self.assertLess(self.so.slow_stochastic()[37], 99)


if __name__ == "__main__":
    unittest.main()
