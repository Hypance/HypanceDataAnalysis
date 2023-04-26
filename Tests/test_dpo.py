import pandas as pd
import numpy as np
import unittest
from hyta.dpo import DPO


class Test_DetrendedPriceOscillator(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.df = pd.read_excel("Tests/files/DPO.xlsx")

    @classmethod
    def tearDownClass(cls) -> None:
        del cls.df

    def test_dpo_ma(self):
        original = np.array(self.df["MA-DPO"][19:])
        test = DPO(list(self.df["close"]), 20).moving_average()
        self.assertAlmostEqual(original[-1], test[-1])
        self.assertGreaterEqual(np.nanmin(test), 0)
        self.assertEqual(len(original), len(test))
        self.assertIsInstance(test, np.ndarray)

    def test_closes(self):
        original = np.array(self.df["CLOSES-DPO"][19:])
        test = DPO(list(self.df["close"]), 20).closes()
        self.assertAlmostEqual(original[-1], test[-1])
        self.assertEqual(len(original), len(test))
        self.assertIsInstance(test, np.ndarray)

    def test_dpo(self):
        original = np.array(self.df["DPO"][19:])
        test = DPO(list(self.df["close"]), 20).dpo()
        self.assertAlmostEqual(original[-1], test.iloc[-1])
        self.assertIsInstance(test, pd.Series)

        # Testing output arrays element counts.
        self.assertEqual(len(original), len(test))


if __name__ == "__main__":
    unittest.main()
