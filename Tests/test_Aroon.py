import pandas as pd
from aroon import Aroon
import unittest

class TestAroon(unittest.TestCase):
    '''
        In this class, testing the following things:
        Element values are equal and is in the same index.
        Returns the same length data comparing to original data
        Returning list is same type as we want(pandas series)
        '''

    @classmethod
    def setUpClass(cls) -> None:
        cls.df = pd.read_excel("Tests/files/Aroon.Oscillator.xls")

    @classmethod
    def tearDownClass(cls) -> None:
        del cls.df

    def test_aroon_up(self):
        originalAroonUp = pd.Series(self.df["Aroon Up"])
        testAroonUp = Aroon(self.df["Adj Close"]).aroon_up()

        self.assertAlmostEqual(originalAroonUp[26], testAroonUp[26])

        self.assertAlmostEqual(originalAroonUp.iloc[-1], testAroonUp.iloc[-1], places=7)

        self.assertEqual(len(originalAroonUp), len(testAroonUp))

        self.assertIsInstance(testAroonUp, pd.Series)

    def test_aroon_down(self):
        originalAroonDown = pd.Series(self.df["Aroon Down"])
        testAroonDown = Aroon(self.df["Adj Close"]).aroon_down()

        self.assertAlmostEqual(originalAroonDown[26], testAroonDown[26])

        self.assertAlmostEqual(originalAroonDown.iloc[-1], testAroonDown.iloc[-1], places=7)

        self.assertEqual(len(originalAroonDown), len(testAroonDown))

        self.assertIsInstance(testAroonDown, pd.Series)


    def test_aroon_oscilattor(self):
        originalAroonOscilattor = pd.Series(self.df["Aroon Oscillator"])
        testAroonOscilattor = Aroon(self.df["Adj Close"]).aroon_oscilattor()

        self.assertAlmostEqual(originalAroonOscilattor[26], testAroonOscilattor[26])

        self.assertAlmostEqual(originalAroonOscilattor.iloc[-1], testAroonOscilattor.iloc[-1], places=7)

        self.assertEqual(len(originalAroonOscilattor), len(testAroonOscilattor))

        self.assertIsInstance(testAroonOscilattor, pd.Series)

    if __name__ == "_main_":
         unittest.main()
