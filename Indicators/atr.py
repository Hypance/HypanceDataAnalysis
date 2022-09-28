#!/usr/bin/env python
# coding: utf-8

# import pandas as pd
# import numpy as np
# 
# class ATR:
#    
#     def __init__(self, data_all):
#         self.data_all = data_all
#       
# 
#     def AverageTrueRange(self,data_all):
#    
#         #True Range için yapılacak hesaplamaları TR listesine atalım.
#         TR=[abs(data_all[1][0]-data_all[2][0])]            
#         for i in range(1,30):
#             TR.append(max(abs(data_all[0][i-1]-data_all[1][i]),
#                          abs(data_all[0][i-1]-data_all[2][i]),
#                          abs(data_all[1][i]-data_all[2][i])))
#             
#         ATR=[]
#         ATR.append(np.mean(TR[0:14]))
#         for i in range(16):
#             ATR.append((ATR[i]*13+TR[i+14])/14)
#             
#         d = {
#             "Close": data_close,
#             "High": data_high,
#             "Low": data_low,
#             "TR": pd.Series(TR, index=[i for i in range(30)]),
#             "ATR": pd.Series(ATR, index=[i for i in range(13,30)]),
#             }
#         df=pd.DataFrame(data=d, index=[i for i in range(30)])
#         
#        
# 
#        
#         return df[13:].reset_index()
# 
# 
# 
# path=r"/Users/anilmehmetuyar/Downloads/ATR.xlsx"
# data=pd.read_excel(path)
# data_close = data['Close'].to_list()
# data_high = data['High'].to_list()
# data_low = data['Low'].to_list()
# data_all=np.array([data_close,data_high,data_low])
# Result=ATR(data_all)
# print(Result.AverageTrueRange(data_all))

# In[ ]:




