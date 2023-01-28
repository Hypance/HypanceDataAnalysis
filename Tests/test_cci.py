import unittest
import pandas as pd
from hyta.CCI import CCI

    
class TestCCI(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.path = "Tests/files/CCI.xlsx"
        cls.data = pd.read_excel(cls.path)

    @classmethod
    def tearDownClass(cls):
        del cls.data

    def setUp(self) -> None:
        self.high = self.data["High"]
        self.low = self.data["Low"]
        self.close = self.data["Close"]
        self.CCI_data = CCI(self.high, self.low, self.close)
        self.cci = CCI(
            self.data["High"], self.data["Low"], self.data["Close"], period=20)

    def tearDown(self):
        del self.cci
        
  
def test_TP(self):
        self.assertAlmostEqual(
            self.cci.TP()[24], self.data["TP"][24])
        self.assertGreater(self.cci.TP()[25], -1)
        self.assertLess(self.cci.TP()[28], 30)

def test_SMA(self):
        self.assertAlmostEqual(
            self.cci.SMA()[24], self.data["SMA"][24])
        self.assertGreater(self.cci.SMA()[25], -1)
        self.assertLess(self.cci.SMA()[28], 30)


def test_MD(self):
        self.assertAlmostEqual(
            self.cci.MD()[23], self.data["MD"][23])
        self.assertGreater(self.cci.MD()[27], -1)
        self.assertLess(self.cci.MD()[28], 1)

def test_CCI(self):
        self.assertAlmostEqual(
            self.cci.CCI()[24], self.data["CCI"][24])
        self.assertGreater(self.cci.CCI()[25], -1)
        self.assertLess(self.cci.CCI()[29], 1)


if __name__ == "__main__":
    unittest.main()
        
