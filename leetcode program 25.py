#You are given an integer n. There are n rooms numbered from 0 to n - 1.
#You are given a 2D integer array meetings where meetings[i] = [starti, endi] 
# means that a meeting will be held during the half-closed time interval
#  [starti, endi). All the values of starti are unique.
#Meetings are allocated to rooms in the following manner:
#Each meeting will take place in the unused room with the lowest number.
#If there are no available rooms, the meeting will be delayed until a room becomes free.
#  The delayed meeting should have the same duration as the original meeting.
#When a room becomes unused, meetings that have an earlier original start time 
# should be given the room.
#Return the number of the room that held the most meetings. If there are multiple rooms,
#  return the room with the lowest number.
#A half-closed interval [a, b) is the interval between a and b 
# including a and not including b.

from typing import List
import heapq

class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort()  # sort by start time

        available = list(range(n))          # free rooms
        heapq.heapify(available)

        busy = []  # (end_time, room)
        count = [0] * n

        for start, end in meetings:
            duration = end - start

            # Free rooms that have completed meetings
            while busy and busy[0][0] <= start:
                _, room = heapq.heappop(busy)
                heapq.heappush(available, room)

            if available:
                room = heapq.heappop(available)
                heapq.heappush(busy, (end, room))
            else:
                end_time, room = heapq.heappop(busy)
                new_end = end_time + duration
                heapq.heappush(busy, (new_end, room))

            count[room] += 1

        # room with max meetings, smallest index if tie
        max_meetings = max(count)
        for i in range(n):
            if count[i] == max_meetings:
                return i
