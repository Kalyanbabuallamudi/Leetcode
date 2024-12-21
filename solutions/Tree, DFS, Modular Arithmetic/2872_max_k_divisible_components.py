from typing import List
from collections import defaultdict

class Solution:
    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:
        # Build adjacency list
        graph = defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        
        self.components = 0
        
        # DFS helper function
        def dfs(node: int, parent: int) -> int:
            total = values[node]
            # Traverse all the neighbors
            for neighbor in graph[node]:
                if neighbor == parent:
                    continue  # Skip the parent node
                total += dfs(neighbor, node)  # Recursively accumulate the total value
            # If the total value is divisible by k, count this as a valid component
            if total % k == 0:
                self.components += 1
                return 0  # Return 0 because this component is now fully processed
            return total
        
        # Start DFS from the first node (node 0)
        dfs(0, -1)
        return self.components


# This Code is Contributed by Kalyan Babu Allamudi