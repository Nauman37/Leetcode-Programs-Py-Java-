#You have a grid of size n x 3 and you want to paint each cell of the grid with exactly one of the three colors:
#Red, Yellow, or Green while making sure that no two adjacent cells have the same color 
#(i.e., no two cells that share vertical or horizontal sides have the same color).
#Given n the number of rows of the grid, return the number of ways you can paint this grid. 
#As the answer may grow large, the answer must be computed modulo 109 + 7.
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
