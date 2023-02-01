import unittest
import pandas as pd
from hyta.SMA import SMA

class TestSMA(unittest.TestCase):
  

  @classmethod
  
  def setUpClass(cls):
    cls.path="Tests/files/Sma.xlsx"
    cls.data=pd.read_excel(cls.path)

  @classmethod
  def tearDownClass(cls):
    del cls.data
    

  def setUp(self)->None:
    self.close=self.data["close"]
    self.sma=SMA(self.data["close"], period=5).Sma()
    
  def tearDown(self):
    del self.sma

  def test_sma(self):
    self.assertAlmostEqual(self.sma[10],self.data["sma"][10])
    self.assertGreater(self.sma[10],-1)
    self.assertLess(self.sma[15],50)
      

if __name__ =='__main__':
    unittest.main()
