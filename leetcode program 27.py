#A 3 x 3 magic square is a 3 x 3 grid filled with distinct numbers from 1 to 9 such that each row, 
#column, and both diagonals all have the same sum. Given a row x col grid of integers, 
#how many 3 x 3 magic square subgrids are there? Note: while a magic square can only contain numbers from 1 to 9, grid may contain numbers up to 15.

from typing import List

class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        count = 0

        def is_magic(r, c):
            nums = set()
            for i in range(3):
                for j in range(3):
                    val = grid[r + i][c + j]
                    if val < 1 or val > 9:
                        return False
                    nums.add(val)
            if len(nums) != 9:
                return False

            s = sum(grid[r][c:c+3])

            for i in range(3):
                if sum(grid[r + i][c:c+3]) != s:
                    return False
                if sum(grid[r + x][c + i] for x in range(3)) != s:
                    return False

            if grid[r][c] + grid[r+1][c+1] + grid[r+2][c+2] != s:
                return False
            if grid[r][c+2] + grid[r+1][c+1] + grid[r+2][c] != s:
                return False

            return True

        for i in range(rows - 2):
            for j in range(cols - 2):
                if grid[i + 1][j + 1] == 5 and is_magic(i, j):
                    count += 1

        return count
