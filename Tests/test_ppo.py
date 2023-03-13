import unittest
import pandas as pd
from hyta.ppo import PPO


class TestPPO(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data = pd.read_excel("Tests/files/PPO.xls")

    @classmethod
    def tearDownClass(cls):
        del cls.data

    def setUp(self) -> None:
        self.close = self.data["Close"]
        self.ppo_data = PPO(close=self.close)
        self.fix1_number = 2
        self.fix2_number = 23

    def test_ema12(self):
        self.result_ema12 = self.ppo_data.ema_12()
        self.assertAlmostEqual(self.result_ema12[0], self.data["Close"][0])
        self.assertAlmostEqual(
            self.result_ema12[self.fix1_number],
            self.data["EMA12"][self.fix1_number],
            places=5,
        )
        self.assertAlmostEqual(
            self.result_ema12[self.fix2_number],
            self.data["EMA12"][self.fix2_number],
            places=5,
        )
        self.assertIsInstance(self.result_ema12, pd.Series)

    def test_ema26(self):
        self.result_ema26 = self.ppo_data.ema_26()
        self.assertAlmostEqual(
            self.result_ema26[self.fix1_number],
            self.data["EMA26"][self.fix1_number],
            places=5,
        )
        self.assertAlmostEqual(
            self.result_ema26[self.fix2_number],
            self.data["EMA26"][self.fix2_number],
            places=5,
        )
        self.assertIsInstance(self.result_ema26, pd.Series)

    def test_ppo(self):
        self.result_ppo = self.ppo_data.ppo()
        self.assertAlmostEqual(
            self.result_ppo[self.fix1_number],
            self.data["PPO"][self.fix1_number],
            places=5,
        )
        self.assertAlmostEqual(
            self.result_ppo[self.fix2_number],
            self.data["PPO"][self.fix2_number],
            places=5,
        )
        self.assertIsInstance(self.result_ppo, pd.Series)


if __name__ == "__main__":
    unittest.main()
