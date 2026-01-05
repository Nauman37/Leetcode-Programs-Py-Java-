#You are given an n x n integer matrix. You can do the following operation any number of times:
#Choose any two adjacent elements of matrix and multiply each of them by -1.
#Two elements are considered adjacent if and only if they share a border.
#Your goal is to maximize the summation of the matrix's elements. 
#Return the maximum sum of the matrix's elements using the operation mentioned above.

from typing import List

class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        total = 0
        neg_count = 0
        min_abs = float('inf')

        for row in matrix:
            for val in row:
                total += abs(val)
                if val < 0:
                    neg_count += 1
                min_abs = min(min_abs, abs(val))

        if neg_count % 2 == 0:
            return total
        else:
            return total - 2 * min_abs
