import unittest
import pandas as pd
from hyta.bollinger import Bollinger

class TestBollinger(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.df = pd.read_excel("Tests/files/bollinger.xlsx")
        cls.indicator = Bollinger(cls.df,cls.df["Close"])

    @classmethod
    def tearDownClass(cls):
        del cls.df
        del cls.indicator

    def test_bollinger(self):
        pd.testing.assert_series_equal(self.df["Upper"],self.indicator.bands()[0],check_names=False)
        pd.testing.assert_series_equal(self.df["Lower"],self.indicator.bands()[1],check_names=False)
        
        # Checks if the upper band is greater than the lower band
        self.assertGreaterEqual(self.indicator.bands()[0][25],self.indicator.bands()[1][25])
        self.assertGreaterEqual(self.indicator.bands()[0][24],self.indicator.bands()[1][24])

        self.assertIsInstance(self.indicator.bands()[0],pd.Series)
        self.assertIsInstance(self.indicator.bands()[1],pd.Series)

        self.assertEqual(len(self.df),len(self.indicator.bands()[0].tolist()))
        self.assertEqual(len(self.df),len(self.indicator.bands()[1].tolist()))

if __name__ == "__main__":
    unittest.main()
    