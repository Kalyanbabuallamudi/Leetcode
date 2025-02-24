from collections import defaultdict, deque
from typing import List

class Solution:
    def mostProfitablePath(self, edges: List[List[int]], bob: int, amount: List[int]) -> int:
        def dfs(node, parent, depth):
            """Perform DFS to record depths and paths."""
            depths[node] = depth
            for neighbor in graph[node]:
                if neighbor != parent:
                    parent_map[neighbor] = node
                    dfs(neighbor, node, depth + 1)

        def calculate_profit(node, parent, current_profit):
            """DFS to calculate the maximum profit Alice can collect."""
            current_profit += amount[node]
            if len(graph[node]) == 1 and node != 0:  # Leaf node
                self.max_profit = max(self.max_profit, current_profit)
            for neighbor in graph[node]:
                if neighbor != parent:
                    calculate_profit(neighbor, node, current_profit)

        # Build the graph
        graph = defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        # Step 1: Record depth of each node and parent-child relationships
        depths = {}
        parent_map = {}
        dfs(0, -1, 0)

        # Step 2: Mark Bob's path and adjust the amount array
        bob_path = set()
        current = bob
        while current != -1:
            bob_path.add(current)
            current = parent_map.get(current, -1)

        alice_time = {node: depths[node] for node in bob_path}
        bob_time = {node: depths[bob] - depths[node] for node in bob_path}

        for node in bob_path:
            if alice_time[node] == bob_time[node]:  # Alice and Bob meet
                amount[node] //= 2
            elif alice_time[node] > bob_time[node]:  # Bob opens first
                amount[node] = 0

        # Step 3: Calculate the maximum profit for Alice
        self.max_profit = float('-inf')
        calculate_profit(0, -1, 0)

        return self.max_profit


# This Code is Contributed by Kalyan Babu Allamudi