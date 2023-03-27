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
        original_gain = pd.Series(self.df["Avg. Gain"])
        test_gain = RSI(self.df["Close"]).gain_calculator()

        self.assertAlmostEqual(original_gain[14], test_gain[13])

        self.assertAlmostEqual(original_gain.iloc[-1], test_gain.iloc[-1], places=7)

        self.assertEqual(len(original_gain), len(test_gain))

        self.assertIsInstance(test_gain, pd.Series)

    def test_loss_calculator(self):
        original_loss = pd.Series(self.df["Avg. Loss"])
        test_loss = RSI(self.df["Close"]).loss_calculator()

        self.assertAlmostEqual(original_loss[14], test_loss[13])

        self.assertAlmostEqual(original_loss.iloc[-1], test_loss.iloc[-1], places=7)

        self.assertEqual(len(original_loss), len(test_loss))

        self.assertIsInstance(test_loss, pd.Series)

    def test_rsi(self):
        original_rsi = pd.Series(self.df["RSI"])
        test_rsi = RSI(self.df["Close"]).rsi()

        self.assertAlmostEqual(original_rsi[14], test_rsi[13])

        self.assertAlmostEqual(original_rsi.iloc[-1], test_rsi.iloc[-1], places=7)

        self.assertEqual(len(original_rsi), len(test_rsi))

        self.assertIsInstance(test_rsi, pd.Series)
        
    if __name__ == "_main_":
        unittest.main()
