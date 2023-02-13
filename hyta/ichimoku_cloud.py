import pandas as pd


class IchimokuCloud:
    """
    The best settings for Ichimoku 5 min chart is standard default settings 9-26-52,
    where 9 is for the Conversion Line ( Tenkan-sen), 26 for the Base Line (Kyun-sen ), and 52 for the Leading Span B (Senkou Span B).
    The best Ichimoku settings for scalping and 1-minute chart are 12-24-120,
    where 12 is for the Conversion Line ( Tenkan-sen), 24 for the Base Line (Kyun-sen ), and 120 for the Leading Span B (Senkou Span B).
    """

    def __init__(
        self,
        closes_list: list,
        lowest_list: list,
        higest_list: list,
        period_list: list = [9, 26, 52, 26],
    ):
        self.lowest_list = lowest_list
        self.higest_list = higest_list
        self.closes_list = closes_list
        self.ts_period = period_list[0]
        self.ks_period = period_list[1]
        self.ssb_period = period_list[2]
        self.cs_period = period_list[3]

    def __founder_higest_price(self, day):
        # This function find the higest price in the past
        return float(max(self.higest_list[-1 : -(day + 1) : -1]))

    def __founder_lowest_price(self, day):
        # This function find the lowest price in the past
        return float(min(self.lowest_list[-1 : -(day + 1) : -1]))

    def __tenkan_sen(self) -> float:
        # the formula of Tenkan Sen => the sum of the higest and lowest price of last 9 days is divied by 2.
        tenkan_sen = (
            self.__founder_higest_price(self.ts_period)
            + self.__founder_lowest_price(self.ts_period)
        ) / 2
        return tenkan_sen

    def __kijun_sen(self) -> float:
        # the formula of Kijun Sen => the sum of the higest and lowest price of last 26 days is divied by 2.
        kijun_sen = (
            self.__founder_higest_price(self.ks_period)
            + self.__founder_lowest_price(self.ks_period)
        ) / 2
        return kijun_sen

    def __senkou_span_A(self) -> float:
        # the formula of Senkou Span A => the sum of Tenkan Sen and Kijun Sen is divied by 2.
        senkou_span_A = (self.__tenkan_sen() + self.__kijun_sen()) / 2
        return senkou_span_A

    def __senkou_span_B(self) -> float:
        # the formula of Senkou Span B => the sum of the higest and lowest price of last 56 days is divied by 2.
        senkou_span_B = (
            self.__founder_higest_price(self.ssb_period)
            + self.__founder_lowest_price(self.ssb_period)
        ) / 2
        return senkou_span_B

    def __cikou_span(self) -> float:
        # the formula of Cikou Span => Finds the closing value of 26 days ago.
        cikou_span = self.closes_list[-self.cs_period]
        return cikou_span

    def ichimoku_cloud(self) -> pd.Series:
        # this create a pandas series and return.
        functions_name = [
            "Tenkan Sen",
            "Kijun Sen",
            "Senkou Span A",
            "Senkou Span B",
            "Cikou Span",
        ]
        functions_values = [
            self.__tenkan_sen(),
            self.__kijun_sen(),
            self.__senkou_span_A(),
            self.__senkou_span_B(),
            self.__cikou_span(),
        ]
        ichimoku_cloud = pd.Series(functions_values, index=functions_name)

        return ichimoku_cloud
