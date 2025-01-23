from typing import List

class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        row_counts = [0] * rows
        col_counts = [0] * cols
        
        # Count the number of servers in each row and column
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    row_counts[i] += 1
                    col_counts[j] += 1
        
        # Count servers that can communicate
        count = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1 and (row_counts[i] > 1 or col_counts[j] > 1):
                    count += 1
        
        return count


# This Code is contributed by Kalyan Babu Allamudi