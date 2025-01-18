from collections import deque
from typing import List

class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # Right, Left, Down, Up
        cost = [[float('inf')] * n for _ in range(m)]
        deque_queue = deque([(0, 0, 0)])  # (row, col, cost)
        cost[0][0] = 0

        while deque_queue:
            x, y, curr_cost = deque_queue.popleft()

            for i, (dx, dy) in enumerate(directions):
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n:
                    new_cost = curr_cost if grid[x][y] == i + 1 else curr_cost + 1
                    if new_cost < cost[nx][ny]:
                        cost[nx][ny] = new_cost
                        if grid[x][y] == i + 1:
                            deque_queue.appendleft((nx, ny, new_cost))
                        else:
                            deque_queue.append((nx, ny, new_cost))

        return cost[m - 1][n - 1]

# This Code is Contributed by Kalyan Babu Allamudi