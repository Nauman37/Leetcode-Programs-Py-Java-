#You are given a positive integer n, representing an n x n city. You are also given a 2D grid buildings, 
# where buildings[i] = [x, y] denotes a unique building located at coordinates [x, y].
#A building is covered if there is at least one building in all four directions: left, right, above, and below.
#Return the number of covered buildings.

from typing import List
from collections import defaultdict
import bisect

class Solution:
    def countCoveredBuildings(self, n: int, buildings: List[List[int]]) -> int:
        if not buildings:
            return 0

        # Count multiplicity of each coordinate (if duplicates exist)
        point_count = defaultdict(int)
        for x, y in buildings:
            point_count[(x, y)] += 1

        unique_points = list(point_count.keys())

        # Build row and column maps: x -> sorted list of y's, y -> sorted list of x's
        x_to_ys = defaultdict(set)
        y_to_xs = defaultdict(set)

        for x, y in unique_points:
            x_to_ys[x].add(y)
            y_to_xs[y].add(x)

        # Convert sets to sorted lists for binary search / index checks
        for x in x_to_ys:
            x_to_ys[x] = sorted(x_to_ys[x])
        for y in y_to_xs:
            y_to_xs[y] = sorted(y_to_xs[y])

        covered_count = 0

        for x, y in unique_points:
            ys = x_to_ys[x]
            xs = y_to_xs[y]

            # Position of y in this row (same x)
            yi = bisect.bisect_left(ys, y)
            has_left = yi > 0
            has_right = yi + 1 < len(ys)

            # Position of x in this column (same y)
            xi = bisect.bisect_left(xs, x)
            has_above = xi > 0
            has_below = xi + 1 < len(xs)

            if has_left and has_right and has_above and has_below:
                # If you want to count each building instance, multiply by point_count[(x, y)]
                covered_count += point_count[(x, y)]

        return covered_count