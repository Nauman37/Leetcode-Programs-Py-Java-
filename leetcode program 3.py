#You are given a 0-indexed integer array nums and an integer p. 
# Find p pairs of indices of nums such that the maximum difference amongst all the pairs is minimized.
#  Also, ensure no index appears more than once amongst the p pairs.
# Note that for a pair of elements at the index i and j,
#  the difference of this pair is |nums[i] - nums[j]|, where |x| represents the absolute value of x.
# Return the minimum maximum difference among all p pairs. We define the maximum of an empty set to be zero.

from typing import List

class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        nums.sort()
        n=len(nums)

        def can_max(diff:int)->bool:
            count = 0
            i = 0
            while i + 1 < n:
                #can we form atleast p pairs with max diff <= diff ?
                if nums[ i + 1 ]-nums[i] <= diff:
                    count += 1
                    i += 2
                else:
                    i += 1
                if count >= p:
                    return True
            return False

        if p == 0:
            return 0

        left,right = 0,nums[ -1 ]-nums[ 0 ]#Possible diff range after the sorting
        ans=right
        while left <= right:
            mid=(left + right)//2
            if can_max(mid):
                ans=mid
                right = mid - 1
            else:
                left = mid + 1
        return ans