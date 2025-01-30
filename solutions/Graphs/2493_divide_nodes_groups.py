from collections import defaultdict, deque

class Solution:
    def magnificentSets(self, n: int, edges: List[List[int]]) -> int:
        # Build adjacency list
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        def bfs(node):
            visited = [-1] * (n + 1)
            visited[node] = 0
            queue = deque([node])
            max_depth = 0

            while queue:
                curr = queue.popleft()
                for neighbor in graph[curr]:
                    if visited[neighbor] == -1:
                        visited[neighbor] = visited[curr] + 1
                        max_depth = max(max_depth, visited[neighbor])
                        queue.append(neighbor)
                    elif abs(visited[neighbor] - visited[curr]) != 1:
                        return -1
            return max_depth + 1

        visited_global = [-1] * (n + 1)
        max_groups = 0

        for i in range(1, n + 1):
            if visited_global[i] == -1:
                # Perform BFS for connected components
                stack = [i]
                component = []
                while stack:
                    node = stack.pop()
                    if visited_global[node] == -1:
                        visited_global[node] = 1
                        component.append(node)
                        stack.extend(graph[node])

                # Try to determine the max depth for the component
                component_depth = 0
                for node in component:
                    depth = bfs(node)
                    if depth == -1:
                        return -1
                    component_depth = max(component_depth, depth)
                max_groups += component_depth

        return max_groups

# This code is contributed by Kalyan Babu Allamudi