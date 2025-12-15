#The password complexity of the computer with index 0 is denoted as T=complexity[0].
#If there exists a computer with an index greater than 0 whose password complexity is
# less than or equal to T, then we should pick the one with the smallest password complexity.
#  Since no computer has a smaller complexity than that, it can never be unlocked, so the answer is 0.
# If no such computer exists, then every computer can be unlocked by computer 0 at the start, and the rest can be unlocked in any order. Thus, the answer is (n−1)!.
from typing import List

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