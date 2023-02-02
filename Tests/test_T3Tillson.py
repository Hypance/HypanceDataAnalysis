import pandas as pd
from hyta.t3tillson import t3Tillson
import unittest

class TestT3Tillson(unittest.TestCase):
    '''
          In these tests, testing the following things:
          Element values are equal and is in the same index.
          Returns the same length data comparing to original data
          Returning list is same type as we want(pandas series)
    '''
    
    @classmethod
    def setUpClass(cls) -> None:
        cls.df = pd.read_excel("Tests/files/t3tillson.xlsx")
    @classmethod
    def tearDownClass(cls) -> None:
        del cls.df

    def test_ema1(self):
        originalEma1 = pd.Series(self.df["ema1 t3"])
        testEma1 = t3Tillson(self.df["close"]).ema1()

        self.assertAlmostEqual(originalEma1[100], testEma1[100])

        self.assertAlmostEqual(originalEma1.iloc[-1], testEma1.iloc[-1], places=7)

        self.assertEqual(len(originalEma1), len(testEma1))

        self.assertIsInstance(testEma1, pd.Series)



    def test_ema2(self):
        originalEma2 = pd.Series(self.df["ema2 t3"])
        testEma2 = t3Tillson(self.df["ema1 t3"]).ema2()

        self.assertAlmostEqual(originalEma2[100], testEma2[100])

        self.assertAlmostEqual(originalEma2[-1], testEma2[-1], places=7)

        self.assertEqual(len(originalEma2), len(testEma2))

        self.assertIsInstance(testEma2, pd.Series)


    def test_ema3(self):
        originalEma3 = pd.Series(self.df["ema3 t3"])
        testEma3 = t3Tillson(self.df["ema2 t3"]).ema3()

        self.assertAlmostEqual(originalEma3[100], testEma3[100])

        self.assertAlmostEqual(originalEma3[-1], testEma3[-1], places=7)

        self.assertEqual(len(originalEma3), len(testEma3))

        self.assertIsInstance(testEma3, pd.Series)


    def test_ema4(self):
        originalEma4 = pd.Series(self.df["ema4 t3"])
        testEma4 = t3Tillson(self.df["ema3 t3"]).ema4()

        self.assertAlmostEqual(originalEma4[100], testEma4[100])

        self.assertAlmostEqual(originalEma4[-1], testEma4[-1], places=7)

        self.assertEqual(len(originalEma4), len(testEma4))

        self.assertIsInstance(testEma4, pd.Series)

    def test_ema5(self):
        originalEma5 = pd.Series(self.df["ema5 t3"])
        testEma5 = t3Tillson(self.df["ema4 t3"]).ema5()

        self.assertAlmostEqual(originalEma5[100], testEma5[100])

        self.assertAlmostEqual(originalEma5[-1], testEma5[-1], places=7)

        self.assertEqual(len(originalEma5), len(testEma5))

        self.assertIsInstance(testEma5, pd.Series)


    def test_ema6(self):
        originalEma6 = pd.Series(self.df["ema6 t3"])
        testEma6 = t3Tillson(self.df["ema5 t3"]).ema6()

        self.assertAlmostEqual(originalEma6[100], testEma6[100])

        self.assertAlmostEqual(originalEma6[-1], testEma6[-1], places=7)

        self.assertEqual(len(originalEma6), len(testEma6))

        self.assertIsInstance(testEma6, pd.Series)

    def test_T3(self):
        originalT3 = pd.Series(self.df["ema1 t3"])
        testT3= t3Tillson(self.df["t3"]).T3()

        self.assertAlmostEqual(originalT3[100], testT3[100])

        self.assertAlmostEqual(originalT3[-1], testT3[-1], places=7)

        self.assertEqual(len(originalT3), len(testT3))

        self.assertIsInstance(testT3, pd.Series)

    if __name__ == "_main_":
         unittest.main()