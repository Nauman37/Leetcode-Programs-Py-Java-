#You are given an array of n strings strs, all of the same length.
#The strings can be arranged such that there is one on each line, making a grid.
#For example, strs = ["abc", "bce", "cae"] can be arranged as follows:
#abcbcecae
#You want to delete the columns that are not sorted lexicographically. 
# In the above example (0-indexed), columns 0 ('a', 'b', 'c') and 2 ('c', 'e', 'e') are sorted,
#  while column 1 ('b', 'c', 'a') is not, so you would delete column 1.
#Return the number of columns that you will delete.

from ast import List

class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        rows = len(strs)
        cols = len(strs[0])
        delete_count = 0
        for c in range(cols):
            for r in range(rows - 1):
                if strs[r][c] > strs[r + 1][c]:
                    delete_count += 1
                    break
        return delete_count