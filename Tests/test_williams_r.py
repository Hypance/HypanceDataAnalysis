import unittest


from hyta.williams_r import WilliamsR

class TestWiliiasR(unittest.TestCase):

    def test_williams_r(self):

        highs = [127.009,127.6159,126.5911,127.3472,128.173,128.4317,127.3671,126.422,126.8995,126.8498,125.646,125.7156,127.1582,127.7154,127.6855,128.2228,128.2725,128.0934,128.2725,127.7353,128.77,129.2873,130.0633,129.1182,129.2873,128.4715,128.0934,128.6506,129.1381,128.6406]
        lowest = [125.3574,126.1633,124.9296,126.0937,126.8199,126.4817,126.034,124.8301,126.3921,125.7156,124.5615,124.5715,125.0689,126.8597,126.6309,126.8001,126.7105,126.8001,126.1335,125.9245,126.9891,127.8148,128.4715,128.0641,127.6059,127.596,126.999,126.8995,127.4865,127.397]
        closes = [127.2876,127.1781,128.0138,127.1085,127.7253,127.0587,127.3273,128.7103,127.8745,128.5809,128.6008,127.9342,128.1133,127.596,127.596,128.6904,128.2725]

        # check the corectness of calculation given predetermined inputs
        result = [-29.56,-32.39,-10.80,-34.19,-18.25,-35.48,-25.47,-1.42,-29.90,-26.94,-26.58,-38.77,-39.04,-59.61,-59.61,-33.17,-43.27]

       
        #check all result
        for i in range(len(closes)):
            r = WilliamsR(current_close = closes[i], lowest_list=lowest[i:i+14], higest_list=highs[i:i+14])
            #check result
            self.assertAlmostEqual(result[i], round(r.WILLIAMS_R(),2))

            #check output type
            self.assertTrue(type(r.WILLIAMS_R()) == float)
            
            #check if result is in limit.
            self.assertGreaterEqual(r.WILLIAMS_R(),-100)
            self.assertLessEqual(r.WILLIAMS_R(),0)

            #check if result is None
            self.assertIsNotNone(r.WILLIAMS_R())


if __name__ == '__main__':
    unittest.main()