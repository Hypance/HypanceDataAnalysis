import numpy as np
import pandas as pd

class PPO:
    def __init__(self,close,ppo_data):
        self.close = close
        self.ppo_data = pd.DataFrame({"Close":self.close})

    def ema_12(self):
        p_12 = round(2/(12+1),ndigits=6)
       
        first = ppo_data["Close"][0]
        ema_12_ilk = (ppo_data["Close"][1] * p_12) + (first * (1-p_12))

        ppo_data["Ema_12"] = 0
        ppo_data["Ema_12"][:2] = [first,ema_12_ilk]

        for i in range(1,len(ppo_data["Close"])):
            ema_12_ilk = (ppo_data["Close"][i] * p_12) + (ppo_data["Ema_12"][i-1] * (1-p_12))
            ppo_data["Ema_12"][i:] = ema_12_ilk
        return pd.DataFrame(ppo_data["Ema_12"])

    def ema_26(self):
        p_26 = round(2/(26+1),ndigits=6)
       
        first = ppo_data["Close"][0]
        ema_26_ilk = (ppo_data["Close"][1] * p_26) + (first * (1-p_26))

        ppo_data["Ema_26"] = 0
        ppo_data["Ema_26"][:2] = [first,ema_26_ilk]

        for i in range(1,len(ppo_data["Close"])):
            ema_26_ilk = (ppo_data["Close"][i] * p_26) + (ppo_data["Ema_26"][i-1] * (1-p_26))
            ppo_data["Ema_26"][i:] = ema_26_ilk
        return pd.DataFrame(ppo_data["Ema_26"])
    
    def ppo(self):
        # Bu kısımda AttributeError: 'Series' object has no attribute 'ema_12'
        # hatası alıyorum. 
        self.ema_12()
        self.ema_26()
        return (ppo_data["Ema_12"] - ppo_data["Ema_26"]) / ppo_data["Ema_12"]