#You are given a 0-indexed 2D integer array of events 
# where events[i] = [startTimei, endTimei, valuei]. The ith event starts at startTimei
#  and ends at endTimei, and if you attend this event, you will receive a value of valuei.
#  You can choose at most two non-overlapping events to attend such that 
# the sum of their values is maximized.
#Return this maximum sum.
#Note that the start time and end time is inclusive: that is, you cannot attend two events
#  where one of them starts and the other ends at the same time. 
# More specifically, if you attend an event with end time t, 
# the next event must start at or after t + 1.



from bisect import bisect_left
from typing import List

class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        
        events.sort()
        n = len(events)
        
        
        starts = [event[0] for event in events]

        suffix_max = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            suffix_max[i] = max(suffix_max[i + 1], events[i][2])
        
        ans = 0
        
        for i in range(n):
            start, end, value = events[i]
            
            idx = bisect_left(starts, end + 1)
            
            total = value + suffix_max[idx]
            ans = max(ans, total)
        
        return ans