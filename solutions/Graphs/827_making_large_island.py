from collections import defaultdict

class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)

        def dfs(x, y, island_id):
            # Perform DFS to mark all cells in the current island and calculate its area
            grid[x][y] = island_id
            area = 1
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < n and grid[nx][ny] == 1:
                    area += dfs(nx, ny, island_id)
            return area

        # Step 1: Identify islands and calculate their areas
        island_id = 2
        island_area = {}
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    island_area[island_id] = dfs(i, j, island_id)
                    island_id += 1

        # Step 2: Calculate the largest possible island
        max_area = max(island_area.values(), default=0)
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 0:
                    # Check adjacent islands
                    seen = set()
                    current_area = 1  # Convert the current 0 to 1
                    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                        nx, ny = i + dx, j + dy
                        if 0 <= nx < n and 0 <= ny < n and grid[nx][ny] > 1:
                            island = grid[nx][ny]
                            if island not in seen:
                                current_area += island_area[island]
                                seen.add(island)
                    max_area = max(max_area, current_area)

        return max_area


# This code is contributed by Kalyan Babu Allamudi