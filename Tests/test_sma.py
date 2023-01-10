import unittest
import pandas as pd
from hyta.SMA import SMA

class TestSMA(unittest.TestCase):
  

  @classmethod
  
  def setUpClass(cls):
    cls.path="Tests/files/datas.xlsx"
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
    self.assertAlmostEqual(sma()[10],self.data["sma"][10])
    self.assertGreater(sma()[10],-1)
    self.assertLess(sma()[15],50)
      

if __name__ =='__main__':
    unittest.main()
