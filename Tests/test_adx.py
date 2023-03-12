import unittest
from hyta.adx import ADX 
import pandas as pd

class TestAdx(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.data = pd.read_excel('Tests/files/cs-adx.xlsx')

    @classmethod
    def tearDownClass(cls):
        del cls.data

    def setUp(self) -> None:
        self.close = self.data["Close"]
        self.low = self.data["Low"]
        self.high = self.data["High"]
        self.adx_data = ADX(self.close,self.low,self.high)

    def test_adx(self):
        self.adx_result = self.adx_data.adx()
        self.assertAlmostEqual(self.adx_result[-1],self.data["ADX"].iloc[-1])