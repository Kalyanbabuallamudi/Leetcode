from typing import List
from collections import deque, defaultdict

class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        reverse_graph = defaultdict(list)
        out_degree = [0] * n
        
        # Reverse the graph and calculate out-degrees
        for node, neighbors in enumerate(graph):
            for neighbor in neighbors:
                reverse_graph[neighbor].append(node)
            out_degree[node] = len(neighbors)
        
        # Collect all terminal nodes (nodes with out-degree 0)
        queue = deque([node for node in range(n) if out_degree[node] == 0])
        safe_nodes = []
        
        # Process the reverse graph
        while queue:
            current = queue.popleft()
            safe_nodes.append(current)
            for neighbor in reverse_graph[current]:
                out_degree[neighbor] -= 1
                if out_degree[neighbor] == 0:
                    queue.append(neighbor)
        
        # Return safe nodes sorted in ascending order
        return sorted(safe_nodes)


# This code is Contributed by Kalyan Babu Allamudi