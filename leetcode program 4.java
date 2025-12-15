/*You are given an integer array prices representing the daily price history of a stock,
where prices[i] is the stock price on the ith day.
A smooth descent period of a stock consists of one or more contiguous days 
such that the price on each day is lower than the price on the preceding day by exactly 1.
The first day of the period is exempted from this rule.
Return the number of smooth descent periods.
*/

MOD=10**9+7
class Solution:
    def countPermutations(self, complexity: List[int]) -> int:
        n=len(complexity)

        for i in range(1,n):
            if complexity[i] <= complexity[0]:
                return 0
        ans=1
        for x in range(1,n):
            ans=(ans*x)%MOD
        return ans
