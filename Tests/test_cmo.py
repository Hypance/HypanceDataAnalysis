import pandas as pd
import numpy as np
from hyta.cmo import CMO
import unittest

class TestCMO(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.df = pd.read_excel("files/CMO.xlsx")

    @classmethod
    def tearDownClass(cls) -> None:
        del cls.df

    '''
    In this module, testing the following things:
    Element values are equal and is in the same index.
    Returns the same length data comparing to original data
    CumulativeUP can not be less than zero.
    Returning list is same type as we want(np.ndarray)
    '''
    def test_cumulativeUp(self):
        originalSUP = np.array(self.df["SUP(t)"])
        testSUP = CMO(self.df["close"]).cumulativeUp()

        self.assertEqual(originalSUP[10],testSUP[10])

        self.assertAlmostEqual(originalSUP[-1],testSUP[-1],places=7)
        
        self.assertEqual(len(originalSUP),len(testSUP))
        
        self.assertGreaterEqual(np.nanmin(testSUP),0.0)
        
        self.assertIsInstance(testSUP,np.ndarray)

    '''
    In this module, testing the following things:
    Element values are equal and is in the same index.
    Returns the same length data comparing to original data
    CumulativeDOWN can not be less than zero.
    Returning list is same type as we want(np.ndarray)
    '''

    def test_cumulativeDown(self):

        originalSUP = np.array(self.df["SDOWN(t)"])
        testSUP = CMO(self.df["close"]).cumulativeDown()

        self.assertEqual(originalSUP[11],testSUP[11])
        
        self.assertAlmostEqual(originalSUP[-1],testSUP[-1],places=7)
        
        self.assertEqual(len(originalSUP),len(testSUP))
        
        self.assertGreaterEqual(np.nanmin(testSUP),0.0)
        
        self.assertIsInstance(testSUP,np.ndarray)

    '''
    In this module, testing the following things:
    Element values are equal and is in the same index.
    Returns the same length data comparing to original data
    CMO can not be less than -100 and greater than 100.
    Returning list is same type as we want(np.ndarray)
    '''

    def test_CMO(self):

        originalSUP = np.array(self.df["CMO"])
        testSUP = CMO(self.df["close"]).cmo()

        self.assertEqual(originalSUP[10],testSUP[10])
        
        self.assertAlmostEqual(originalSUP[-1],testSUP[-1],places=7)
        
        self.assertEqual(len(originalSUP),len(testSUP))
        
        self.assertGreaterEqual(np.nanmin(testSUP),-100)

        self.assertLessEqual(np.nanmax(testSUP),100)
        
        self.assertIsInstance(testSUP,np.ndarray)

        


if __name__ == "__main__":
    unittest.main()
