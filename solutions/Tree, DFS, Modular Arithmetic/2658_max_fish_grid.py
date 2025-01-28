class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        def dfs(r, c):
            # Base case: Out of bounds or land cell
            if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]) or grid[r][c] == 0:
                return 0
            
            # Collect fish from current cell and mark it as visited
            fish = grid[r][c]
            grid[r][c] = 0  # Mark as visited
            
            # Explore all 4 adjacent cells
            fish += dfs(r + 1, c)
            fish += dfs(r - 1, c)
            fish += dfs(r, c + 1)
            fish += dfs(r, c - 1)
            
            return fish
        
        max_fish = 0
        
        # Iterate over all cells in the grid
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] > 0:  # Start DFS from water cells
                    max_fish = max(max_fish, dfs(r, c))
        
        return max_fish

# This code is contributed by Kalyan Babu Allamudi