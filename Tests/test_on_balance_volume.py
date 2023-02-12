import unittest
import pandas as pd 

from hyta.on_balance_volume import OnBalanceVolume


class TestOnBalanceVolume(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.data = pd.read_excel('Tests/files/OnBalanceVolue.xlsx')
        cls.close = cls.data['Adj Close'].to_list()
        cls.volume = cls.data['Volume'].to_list()
        cls.obv = cls.data['OBV'].to_list()

    @classmethod
    def tearDownClass(cls):
        del cls.data
        del cls.close
        del cls.volume
        del cls.obv

    def test_on_balance_volume(self):

        obv_result = OnBalanceVolume(self.close,self.volume,2013)

        self.assertNotAlmostEqual(self.obv[2012],obv_result.on_balance_volume())
        self.assertIsInstance(obv_result.on_balance_volume(),int)


