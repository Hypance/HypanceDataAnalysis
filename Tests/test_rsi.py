import pandas as pd
from hyta.rsi import RSI
import unittest

class TestRSI(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.df = pd.read_excel("files/RSI.xlsx")
    @classmethod
    def tearDownClass(cls) -> None:
        del cls.df

    '''
    In this module, testing the following things:
    Element values are equal and is in the same index.
    Returns the same length data comparing to original data
    Returning list is same type as we want(pandas series)
    '''

    def test_gain_calculator(self):
        originalGAIN = pd.Series(self.df["Avg. Gain"])
        testGAIN = RSI(self.df["Close"]).gain_calculator()

        self.assertAlmostEqual(originalGAIN[14], testGAIN[13])

        self.assertAlmostEqual(originalGAIN[-1], testGAIN[-1], places=7)

        self.assertEqual(len(originalGAIN), len(testGAIN))

        self.assertIsInstance(testGAIN, pd.Series)

    '''
    In this module, testing the following things:
    Element values are equal and is in the same index.
    Returns the same length data comparing to original data
    Returning list is same type as we want(pandas series)
        '''

    def test_loss_calculator(self):
        originalLOSS = pd.Series(self.df["Avg. Loss"])
        testLOSS = RSI(self.df["Close"]).loss_calculator()

        self.assertAlmostEqual(originalLOSS[15], testLOSS[15])

        self.assertAlmostEqual(originalLOSS[-1], testLOSS[-1], places=7)

        self.assertEqual(len(originalLOSS), len(testLOSS))

        self.assertIsInstance(testLOSS, pd.Series)

    '''
    In this module, testing the following things:
    Element values are equal and is in the same index.
    Returns the same length data comparing to original data
    Returning list is same type as we want(pandas series)
    '''

    def test_rsi(self):
        originalRsi = pd.Series(self.df["RSI"])
        testRsi = RSI(self.df["Close"]).rsi()

        self.assertAlmostEqual(originalRsi[15], testRsi[15])

        self.assertAlmostEqual(originalRsi[-1], testRsi[-1], places=7)

        self.assertEqual(len(originalRsi), len(testRsi))

        self.assertIsInstance(testRsi, pd.Series)


    if __name__ == "_main_":
        unittest.main()
