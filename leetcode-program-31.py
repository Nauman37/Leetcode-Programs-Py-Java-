class Solution:
    def numOfWays(self, n: int) -> int:
        MOD = 10**9 + 7

        # Base case for first row
        dpA = 6  # all different colors
        dpB = 6  # first and third same

        for _ in range(1, n):
            newA = (2 * dpA + 2 * dpB) % MOD
            newB = (2 * dpA + 3 * dpB) % MOD
            dpA, dpB = newA, newB

        return (dpA + dpB) % MOD
