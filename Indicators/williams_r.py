def WILLIAMS_R(higest_price_last_14days,lowest_price_last_14days,current_close_price):
    #Williams%R say overbought and oversold
    #Williams%R answer is between 0 to -100. 
    #If anwer goes above -20, this is overbought. If it drops below -80, this is oversold
    #If answer is above -20 and moving below -20, It's a sign that the price might go down.
    #If answer is below -80 and rising above -80, It's a sign that the price might rise.
    #-10 and -90 reference values ​​are more reliable than -20 and -80

    # The formula of Williams%R
    R = (higest_price_last_14days - current_close_price) / (higest_price_last_14days - lowest_price_last_14days) *-100
    
    return R


def founder_higest_price(high_price_list):
    #This function find the higest price of the last 14 days
    return float(max(high_price_list[-1:-15:-1]))

def founder_lowest_price(low_price_list):
    #This function find the lowest price of the last 14 days
    return float(min(low_price_list[-1:-15:-1]))


high_price_list =  input().split(",")
low_price_list = input().split(",")
current_close_price = float(input())

#Print answer of Williams%R
print(WILLIAMS_R(founder_higest_price(high_price_list),founder_lowest_price(low_price_list),current_close_price))
