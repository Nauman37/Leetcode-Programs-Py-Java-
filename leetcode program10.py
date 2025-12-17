#You have n computers. You are given the integer n and a 0-indexed integer array batteries
#where the ith battery can run a computer for batteries[i] minutes.
#You are interested in running all n computers simultaneously using the given batteries.
#Initially, you can insert at most one battery into each computer.
# After that and at any integer time moment, you can remove a battery from a computer
#  and insert another battery any number of times. 
# The inserted battery can be a totally new battery or a battery from another computer. 
# You may assume that the removing and inserting processes take no time.


from typing import List

class Solution:
    def maxRunTime(self, n: int, batteries: List[int]) -> int:
        left, right =0, sum(batteries) // n

        def canRun(t: int) -> bool:
            total = 0
            for b  in batteries:
                total += min(b,t)
            return total >= n * t

        while left < right:
            mid = (left + right+ 1) // 2
            if canRun(mid):
                left = mid
            else:
                right = mid - 1
        return left