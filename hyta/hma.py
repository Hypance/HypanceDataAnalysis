from hyta.wma import WeightedMovingAverage
import math


class HullMovingAverage:
    """ "
    HMAs with shorter periods are often used to identify entry points.
    When the overall trend is up and the HMA turns up, this is a signal to buy long.
    Conversely, when the overall trend is down and the HMA turns down, this is a signal to buy short.
    shoreter period is usually 20.
    """

    """
    Hull Moving Average Formula:
    (A) The First Weighted Moving Average (WMA1):
    WMA1[i] = (Close[i − N + 1] + 2 × Close[i − N + 2] + 3 × Close[i − N + 3] + … + N × Close[i]) / (N × (N + 1) × 0.5) where:
    N = Hull Moving Average look back;
    Index: i ~ Current Bar.
    (B) The Second Weighted Moving Average (WMA2):
    WMA2[i] = (Close[i − M + 1] + 2 × Close[i − M + 2] + 3 × Close[i − M + 3] + … + M × Close[i]) / (M × (M + 1) × 0.5) where:
    M = round(N/2);
    Index: i ~ Current Bar.
    (C) The Hull Moving Average (HMA):
    Delta[i] = 2 × WMA2[i] − WMA1[i];
    HMA[i] = (Delta[i − K + 1] + 2 × Delta[i − K + 2] + 3 × Delta[i − K + 3] + … + K × Delta[i])/(K × (K + 1) × 0.5) where:
    K = round(SquareRoot(N));
    Index: i ~ Current Bar.
    """

    def __init__(self, close_list, period):
        self.close_list = close_list
        self.period = period
        self.wma = WeightedMovingAverage

    def __number_rounder(self, num) -> int:
        # this function round number
        return int(num + 0.5)

    def __wma1(self, number) -> float:
        # Returns the first weighted moving average, using half the period as the length of the moving average

        return self.wma(
            self.close_list[: -number or None], self.__number_rounder(self.period / 2)
        ).weighted_moving_average()

    def __wma2(self, number) -> float:
        # Returns the second weighted moving average, using the period as the length of the moving average

        return self.wma(
            self.close_list[: -number or None], self.period
        ).weighted_moving_average()

    def __raw_hma(self, number) -> float:
        # Returns the raw Hull Moving Average, which is calculated as (2 * wma1) - wma2
        return (2 * self.__wma1(number)) - self.__wma2(number)

    def raw_hma_list(self) -> list:
        raw_hma_list = []
        for i in range(self.__number_rounder(math.sqrt(self.period)), -1, -1):
            raw_hma_list.append(self.__raw_hma(i))

        return raw_hma_list

    def hull_moving_average(self) -> float:
        # Returns the final Hull Moving Average, which is calculated using a weighted moving average of the raw HMAs
        hma = self.wma(
            self.raw_hma_list(), self.__number_rounder(math.sqrt(self.period))
        ).weighted_moving_average()

        return hma
