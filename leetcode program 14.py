# You are given an integer n indicating there are n people numbered from 0 to n - 1. 
# You are also given a 0-indexed 2D integer array meetings where meetings[i] = [xi, yi, timei] 
# indicates that person xi and person yi have a meeting at timei.
#  A person may attend multiple meetings at the same time. Finally, you are given an integer firstPerson.
# Person 0 has a secret and initially shares the secret with a person firstPerson at time 0. 
# This secret is then shared every time a meeting takes place with a person that has the secret. 
# More formally, for every meeting, if a person xi has the secret at timei, 
# then they will share the secret with person yi, and vice versa.
# The secrets are shared instantaneously. That is, a person may receive the secret 
# and share it with people in other meetings within the same time frame.

from typing import List
from collections import defaultdict

class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        # People who currently know the secret
        knows = set([0, firstPerson])

        # Sort meetings by time
        meetings.sort(key=lambda x: x[2])

        i = 0
        while i < len(meetings):
            time = meetings[i][2]

            # Collect all meetings at the same time
            same_time = []
            while i < len(meetings) and meetings[i][2] == time:
                same_time.append(meetings[i])
                i += 1

            # DSU for this time frame
            parent = {}

            def find(x):
                if parent[x] != x:
                    parent[x] = find(parent[x])
                return parent[x]

            def union(x, y):
                px, py = find(x), find(y)
                if px != py:
                    parent[py] = px

            # Initialize DSU nodes
            for x, y, _ in same_time:
                if x not in parent:
                    parent[x] = x
                if y not in parent:
                    parent[y] = y
                union(x, y)

            # Group people by connected components
            groups = defaultdict(list)
            for person in parent:
                groups[find(person)].append(person)

            # If any person in a group knows the secret, all get it
            for group in groups.values():
                if any(p in knows for p in group):
                    knows.update(group)

        return list(knows)
