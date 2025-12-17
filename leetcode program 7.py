#You are given an integer array prices where prices[i] is the price of a stock in dollars on the ith day, and an integer k.
#You are allowed to make at most k transactions, where each transaction can be either of the following:
#Normal transaction: Buy on day i, then sell on a later day j where i < j. You profit prices[j] - prices[i].
#Short selling transaction: Sell on day i, then buy back on a later day j where i < j.
#  You profit prices[i] - prices[j].
#Note that you must complete each transaction before starting another. Additionally, 
# you can't buy or sell on the same day you are selling or buying back as part of a previous transaction.
#Return the maximum total profit you can earn by making at most k transactions.

from typing import List
import math

class Solution:
    def maximumProfit(self, prices: List[int], k: int) -> int:
        n = len(prices)
        if n == 0 or k == 0:
            return 0
        
        dp = [[-math.inf] * 3 for _ in range(k + 1)]
        dp[0][0] = 0

        for price in prices:
            new_dp = [row[:] for row in dp]

            for t in range(k + 1):
                new_dp[t][0] = max(new_dp[t][0], dp[t][0])

                new_dp[t][1] = max(dp[t][1], dp[t][0] - price)

                new_dp[t][2] = max(dp[t][2], dp[t][0] + price)
            
            for t in range(k):
                new_dp[t + 1][0] = max(new_dp[t + 1][0], dp[t][1] + price, dp[t][2]- price)

            dp =new_dp

        return max(dp[t][0] for t in range(k + 1))