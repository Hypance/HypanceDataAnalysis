import pandas as pd

class CMF:
    data_name = 'cs-cmf.xls'
    data = pd.read_excel(data_name)
    # Column adlarını düzeltme
    data.columns.values[4] = "MF_Multiplier"
    data.columns.values[6] = "MF_Volume"
    data.columns.values[7] = "20_period_CMF"

    def __init__(self,close,low,high,volume):
        self.close = close
        self.low = low
        self.high = high
        self.volume = volume
        
    #1. Money Flow Multiplier = [(Close  -  Low) - (High - Close)] /(High - Low) 
    def money_flow_multiplier(close,low,high):
        mfm = ((close - low) - (high - close)) / (high - low)
        return mfm

    # 2. Money Flow Volume = Money Flow Multiplier x Volume for the Period
    def money_flow_volume(mfm, volume):
        mfv = mfm * volume
        return mfv
    
    # 3. 20-period CMF = 20-period Sum of Money Flow Volume / 20 period Sum of Volume 
    for i in range(20):
        result1 = money_flow_multiplier(data.loc[i,"Close"],data.loc[i,"Low"],data.loc[i,"High"])
        result2 = money_flow_volume(result1, data.loc[i, "Volume"])
        CMF = result2.sum() / data["Volume"].sum()
        print(CMF)
