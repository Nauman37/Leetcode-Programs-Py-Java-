import sys
sys.setrecursionlimit(10**7)
from typing import List

class Solution:
    def maxProfit(self, n: int, present: List[int], future: List[int],
                hierarchy: List[List[int]], budget: int) -> int:
        NEG_INF = -10**15

        # Build tree (0-indexed)
        tree = [[] for _ in range(n)]
        for u, v in hierarchy:
            tree[u-1].append(v-1)

        # Merge two knapsack arrays, skipping unreachable entries
        def merge(dpA, dpB):
            merged = [NEG_INF] * (budget + 1)
            # Build lists of indices where dpA/B are reachable
            validA = [i for i, val in enumerate(dpA) if val > NEG_INF]
            validB = [j for j, val in enumerate(dpB) if val > NEG_INF]
            for i in validA:
                a_val = dpA[i]
                for j in validB:
                    if i + j <= budget:
                        # Only update if we have a better profit
                        candidate = a_val + dpB[j]
                        if candidate > merged[i + j]:
                            merged[i + j] = candidate
            return merged

        # DFS: returns (dp0, dp1) for subtree at u
        # dp0 = max profit array if u's parent did NOT buy u
        # dp1 = max profit array if u's parent DID buy u (so u has discount)
        def dfs(u: int):
            # Start with no children processed: zero profit at budget 0
            noDiscount = [0] * (budget + 1)
            withDiscount = [0] * (budget + 1)

            # Process children subtrees
            for v in tree[u]:
                childNo, childYes = dfs(v)
                noDiscount = merge(noDiscount, childNo)
                withDiscount = merge(withDiscount, childYes)

            # Incorporate option to buy u or not
            newDp0 = noDiscount[:]  # parent didn’t buy u
            newDp1 = noDiscount[:]  # parent did buy u (u has discount for itself)
            
            # Option 1: buy u at full price (parent didn’t buy u)
            cost_full = present[u]
            profit_full = future[u] - cost_full
            for b in range(cost_full, budget + 1):
                # Use children profits from the WITH-discount array if u is bought
                val = withDiscount[b - cost_full] + profit_full
                if val > newDp0[b]:
                    newDp0[b] = val
            
            # Option 2: buy u at half price (parent did buy u)
            cost_half = present[u] // 2
            profit_half = future[u] - cost_half
            for b in range(cost_half, budget + 1):
                val = withDiscount[b - cost_half] + profit_half
                if val > newDp1[b]:
                    newDp1[b] = val
            
            return newDp0, newDp1

        # Run DFS from root (0). Root has no parent, so use dp0.
        dp0_root, dp1_root = dfs(0)
        return max(dp0_root)
