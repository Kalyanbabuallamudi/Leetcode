from collections import defaultdict, deque
from typing import List

class Solution:
    def minimumDiameterAfterMerge(self, edges1: List[List[int]], edges2: List[List[int]]) -> int:
        def tree_diameter(edges):
            graph = defaultdict(list)
            for u, v in edges:
                graph[u].append(v)
                graph[v].append(u)

            def bfs(node):
                visited = set()
                queue = deque([(node, 0)])
                farthest_node, max_distance = node, 0

                while queue:
                    current, distance = queue.popleft()
                    visited.add(current)

                    if distance > max_distance:
                        max_distance = distance
                        farthest_node = current

                    for neighbor in graph[current]:
                        if neighbor not in visited:
                            queue.append((neighbor, distance + 1))

                return farthest_node, max_distance

            farthest, _ = bfs(0)
            _, diameter = bfs(farthest)
            return diameter

        diameter1 = tree_diameter(edges1)
        diameter2 = tree_diameter(edges2)

        # Minimum diameter after merging the two trees
        return max((diameter1 + 1) // 2 + (diameter2 + 1) // 2 + 1, diameter1, diameter2)

        
# This Code is Contributed by Kalyan Babu Allamudi