#You are given an integer array nums with the following properties:
#nums.length == 2 * n.
#nums contains n + 1 unique elements.
#Exactly one element of nums is repeated n times.
#Return the element that is repeated n times.from typing import List

class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        seen = set()
        for num in nums:
            if num in seen:
                return num
            seen.add(num)
