import unittest
import pandas as pd
import numpy as np
from hyta.roc import ROC


class TestRateOfChange(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.df = pd.read_excel("Tests/files/ROC.xlsx")
        cls.close = np.array(cls.df["close"])

    @classmethod
    def tearDownClass(cls) -> None:
        del cls.df

    def test_Roc(self):
        # [12:] is necessary to skip the empty values of ROC in Sample Excel.
        original = np.array(self.df["ROC"][12:])
        test = ROC(self.close).roc()
        self.assertIsNotNone(test)
        self.assertAlmostEqual(original[-1], test.iloc[-1])
        self.assertEqual(len(original), len(test))
        self.assertIsInstance(test, pd.Series)


if __name__ == "__main__":
    unittest.main()
