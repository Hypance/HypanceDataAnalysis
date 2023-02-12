import pandas as pd
from hyta.rsi import RSI
import unittest
class TestRSI(unittest.TestCase):
    '''
        In this class, testing the following things:
        Element values are equal and is in the same index.
        Returns the same length data comparing to original data
        Returning list is same type as we want(pandas series)
        '''
    @classmethod
    def setUpClass(cls) -> None:
         cls.df = pd.read_excel("Tests/files/RSI.xlsx")
    @classmethod
    def tearDownClass(cls) -> None:
         del cls.df

    def test_gain_calculator(self):
        originalGAIN = pd.Series(self.df["Avg. Gain"])
        testGAIN = RSI(self.df["Close"]).gain_calculator()

        self.assertAlmostEqual(originalGAIN[14], testGAIN[13])

        self.assertAlmostEqual(originalGAIN.iloc[-1], testGAIN.iloc[-1], places=7)

        self.assertEqual(len(originalGAIN), len(testGAIN))

        self.assertIsInstance(testGAIN, pd.Series)

    def test_loss_calculator(self):
        originalLOSS = pd.Series(self.df["Avg. Loss"])
        testLOSS = RSI(self.df["Close"]).loss_calculator()

        self.assertAlmostEqual(originalLOSS[15], testLOSS[15])

        self.assertAlmostEqual(originalLOSS.iloc[-1], testLOSS.iloc[-1], places=7)

        self.assertEqual(len(originalLOSS), len(testLOSS))

        self.assertIsInstance(testLOSS, pd.Series)

    def test_rsi(self):
        originalRsi = pd.Series(self.df["RSI"])
        testRsi = RSI(self.df["Close"]).rsi()

        self.assertAlmostEqual(originalRsi[15], testRsi[15])

        self.assertAlmostEqual(originalRsi.iloc[-1], testRsi.iloc[-1], places=7)

        self.assertEqual(len(originalRsi), len(testRsi))

        self.assertIsInstance(testRsi, pd.Series)

    if __name__ == "_main_":
        unittest.main()
