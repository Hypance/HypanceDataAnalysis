import numpy as np
import pandas as pd
from hyta.atr import ATR

class DX:
    
    def __init__(self,high:pd.Series,low:pd.Series,close:pd.Series,period:int=14) -> None:
        self.high = high
        self.low = low
        self.close = close
        self.period = period

    def TR(self) -> pd.Series:
        self.dx_data = pd.DataFrame({"TR":TR_cal})
        TR_cal = ATR([self.dx_data[self.high],self.dx_data[self.low],self.dx_data[self.close]],14).true_range()
        self.dx_data["TR"][0] = np.nan
        return self.dx_data["TR"]
    
    def plus_dm(self) -> pd.Series:
        self.dx_data["+DM 1"] = self.dx_data[self.high] - self.dx_data[self.high].shift(1)
        plus_dm = self.dx_data['+DM 1'][self.dx_data['+DM 1'] < 0] = 0
        return plus_dm
    
    def minus_dm(self) -> pd.Series:
        first = [np.NAN]
        
        for i in range(1,len(self.dx_data[self.low])):
            low_diff = self.dx_data[self.low][i-1] - self.dx_data[self.low][i]
            high_diff = self.dx_data[self.high][i] - self.dx_data[self.high][i-1]
            
            if low_diff > high_diff:
                first.append(max(low_diff,0))
            else:
                first.append(0)
        self.dx_data["-DM 1"] = pd.DataFrame({"-DM 1":first})
        return self.dx_data["-DM 1"]
    
    def smoothed_plus_dm14(self):
        first_14_plus_dm = self.dx_data["+DM 1"][:self.period+1].sum()
        second_14_plus_dm = first_14_plus_dm - (first_14_plus_dm/self.period) + self.dx_data["+DM 1"][self.period+1]

        new_dx_Data = np.array([])
        for i in range(self.period):
            new_dx_Data = np.append(new_dx_Data,np.nan)
        new_dx_Data = np.append(new_dx_Data,[first_14_plus_dm,second_14_plus_dm])
        
        for i in range(len(self.dx_data["+DM 1"])-self.period+2):
            other_14_plus_dm = new_dx_Data[-1] - (new_dx_Data[-1]/self.period) + self.dx_data["+DM 1"][i+self.period+2]
            new_dx_Data = np.append(new_dx_Data,other_14_plus_dm)
            self.dx_data["+DM 14"] = pd.DataFrame({"+DM 14":new_dx_Data})
        return self.dx_data["+DM 14"]

    def smoothed_minus_dm14(self):
        first_14_minus_dm  = self.dx_data["-DM 1"][:self.period+1].sum()
        second_14_minus_dm = first_14_minus_dm - (first_14_minus_dm/self.period) + self.dx_data["-DM 1"][self.period+1]

        new_dx_Data = np.array([])
        for i in range(self.period):
            new_dx_Data = np.append(new_dx_Data,np.nan)
        new_dx_Data = np.append(new_dx_Data,[first_14_minus_dm,second_14_minus_dm])
 
        for i in range(len(self.dx_data["-DM 1"])-self.period+2):
            other_14_minus_dm14 = new_dx_Data[-1] - (new_dx_Data[-1]/self.period) + self.dx_data["-DM 1"][i+self.period+2]
            new_dx_Data = np.append(new_dx_Data,other_14_minus_dm14)
            self.dx_data["-DM 14"] = pd.DataFrame({"-DM 14": new_dx_Data })
        return self.dx_data["-DM 14"]
        
    def smoothed_tr_dm14(self):
        first_14_tr = self.dx_data["TR"][:self.period+1].sum()
        second_14_tr = first_14_tr - (first_14_tr/self.period) + self.dx_data["TR"][self.period]

        new_tr_Data = np.array([])
        for i in range(self.period):
            new_tr_Data = np.append(new_tr_Data,np.nan)
        new_tr_Data = np.append(new_tr_Data,[first_14_tr,second_14_tr])
        
        for i in range(len(self.dx_data["New TR"])- self.period+2):
            other_14_tr = new_tr_Data[-1] - (new_tr_Data[-1]/self.period) + self.dx_data["TR"][i+self.period+2]
            new_tr_Data = np.append(new_tr_Data,other_14_tr)
            self.dx_data["Smoothed TR"] = pd.DataFrame({"Smoothed TR":new_tr_Data})
        return pd.DataFrame(self.dx_data["Smoothed TR"])

    def plus_di_14(self):
        plus_di_14 = 100*(self.dx_data["+DM 14"] / self.dx_data["Smoothed TR"])
        return plus_di_14

    def minus_di_14(self):
        minus_di_14 = 100*(self.dx_data["-DM 14"] / self.dx_data["Smoothed TR"])
        return minus_di_14
    
    def di_diff(self):
        di_difference = abs(self.plus_di_14() - self.minus_di_14())
        return di_difference
    
    def di_sum(self):
        di_sum = self.plus_di_14() + self.minus_di_14()
        return di_sum
        
    
    def dx(self):
        dx = abs(100*(self.di_diff() / self.di_sum()))
        return dx