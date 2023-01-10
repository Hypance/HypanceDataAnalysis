import unittest
import pandas as pd
from hyta.ichimoku_cloud import IchimokuCloud



class TestIchimokuCloud(unittest.TestCase):
    
    
    @classmethod
    def setUpClass(cls) -> pd.Series:
        
        cls.data = pd.read_excel('Tests/files/ICHIMOKUCLOUD.xlsx')
        cls.close = cls.data['close'].to_list()
        cls.high = cls.data['high'].to_list()
        cls.low = cls.data['low'].to_list()
        cls.ts = cls.data['tenka_sen'].to_list()
        cls.ks = cls.data['kiju_sen'].to_list()
        cls.spa = cls.data['senkau span a'].to_list()
        cls.spb = cls.data['senkau span b'].to_list()
        cls.cs = cls.data['cikou span'].to_list()
        cls.all = [pd.Series([cls.ts[e],cls.ks[e],cls.spa[e],cls.spb[e],cls.cs[e]],["Tenkan Sen","Kijun Sen","Senkou Span A","Senkou Span B","Cikou Span"]) for e in range(len(cls.close))]
        cls.ic = IchimokuCloud(cls.close,cls.low,cls.high)
    @classmethod
    def tearDownClass(cls):
        del cls.data
        del cls.close
        del cls.high
        del cls.low
        del cls.ts
        del cls.ks
        del cls.spa
        del cls.spb
        del cls.cs
        del cls.all
        del cls.ic       
  

    def test_tenka_sen(self):        
        self.assertAlmostEqual(self.ic.ichimoku_cloud()[0],self.all[-1][0])
        self.assertIsInstance(self.ic.ichimoku_cloud()[0],float)
        self.assertGreater(self.ic.ichimoku_cloud()[0],0)
    def test_kijun_sen(self):        
        self.assertAlmostEqual(self.ic.ichimoku_cloud()[1],self.all[-1][1])
        self.assertIsInstance(self.ic.ichimoku_cloud()[1],float)
        self.assertGreater(self.ic.ichimoku_cloud()[1],0)
    def test_sekou_span_a(self):        
        self.assertAlmostEqual(self.ic.ichimoku_cloud()[2],self.all[-1][2])
        self.assertIsInstance(self.ic.ichimoku_cloud()[2],float)
        self.assertGreater(self.ic.ichimoku_cloud()[2],0)
    def test_senkou_span_b(self):        
        self.assertAlmostEqual(self.ic.ichimoku_cloud()[3],self.all[-1][3])
        self.assertIsInstance(self.ic.ichimoku_cloud()[3],float)
        self.assertGreater(self.ic.ichimoku_cloud()[3],0)
    def test_cikou_span_a(self):       
        self.assertAlmostEqual(self.ic.ichimoku_cloud()[4],self.all[-1][4])
        self.assertIsInstance(self.ic.ichimoku_cloud()[4],float)
        self.assertGreater(self.ic.ichimoku_cloud()[4],0)

    def test_ichimoku_cloud(self):
        self.assertIsInstance(self.ic.ichimoku_cloud(), pd.Series)
        self.assertEqual(len(self.ic.ichimoku_cloud()),len(self.all[-1]))
    
    def test_input_value(self):
        self.assertIsNotNone(self.close[100])
        self.assertIsNotNone(self.low[0])
        self.assertIsNotNone(self.high[1435])
        self.assertIsInstance(self.close, list)
        self.assertIsInstance(self.low, list)
        self.assertIsInstance(self.high, list)

    
if __name__ == '__main__':
    unittest.main()


