#You are given two integer arrays prices and strategy, where:
#prices[i] is the price of a given stock on the ith day.
#strategy[i] represents a trading action on the ith day, where:
#-1 indicates buying one unit of the stock.
#0 indicates holding the stock.
#1 indicates selling one unit of the stock.
#You are also given an even integer k, and may perform at most one modification to strategy. 
# A modification consists of:
#Selecting exactly k consecutive elements in strategy.
#Set the first k / 2 elements to 0 (hold).
#Set the last k / 2 elements to 1 (sell).
#The profit is defined as the sum of strategy[i] * prices[i] across all days.
#
#Return the maximum possible profit you can achieve.
from typing import List
class Solution:
    def maxProfit(self, prices: List[int], strategy: List[int], k: int) -> int:
        n= len(prices)

        original_profit = sum(p * s for p,s in zip(prices,strategy))

        price_prefix = [0] *(n + 1)
        contrib_prefix = [0] * (n + 1)

        for i in range (n):
            price_prefix[i + 1] = price_prefix[i] + prices[i]
            contrib_prefix[i + 1] = contrib_prefix[i] + prices[i] * strategy[i]

        half = k // 2
        max_gain = 0

        for start in range(n - k + 1):
            mid = start + half
            end = start + k

            old = contrib_prefix[end] - contrib_prefix[start]

            new = price_prefix [end] - price_prefix[mid]
            gain = new - old
            max_gain = max(max_gain,gain)
        return original_profit + max_gain