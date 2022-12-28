import unittest
import pandas as pd
from hyta.SMA import SMA

class TestSMA(unittest.TestCase):

  PATH="Tests/files/datas.xlsx"

  @classmethod
  def setUpClass(cls):
    cls.path=PATH
    cls.data=pd.read_excel(cls.path)

  @classmethod
  def tearDownClass(cls):
    del cls.data
    

  def setUp(self)->None:
    self.close=self.data["close"]
    self.SMA_data=SMA(self.close)
    sma=SMA(data["close"])
    
  def tearDown(self):
    del sma

  def test_sma(self):
    self.assertAlmostEqual(sma()[1],self.data["sma"][1])
    self.assertGreater(sma()[1],-1)
    self.assertLess(sma()[4],1)
      

if__name__ =='__main__':
    unittest.main()
