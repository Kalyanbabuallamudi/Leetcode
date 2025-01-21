from typing import List

class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        n = len(grid[0])
        # Prefix sums for both rows
        top_prefix = [0] * n
        bottom_prefix = [0] * n

        top_prefix[0] = grid[0][0]
        bottom_prefix[0] = grid[1][0]

        # Calculate prefix sums
        for i in range(1, n):
            top_prefix[i] = top_prefix[i - 1] + grid[0][i]
            bottom_prefix[i] = bottom_prefix[i - 1] + grid[1][i]

        result = float('inf')

        for i in range(n):
            # Points remaining on the top row (right side of column i)
            top_remaining = top_prefix[-1] - top_prefix[i]
            # Points remaining on the bottom row (left side of column i)
            bottom_remaining = bottom_prefix[i - 1] if i > 0 else 0

            # The second robot takes the maximum of the two possible paths
            second_robot_points = max(top_remaining, bottom_remaining)
            # Minimize the points collected by the second robot
            result = min(result, second_robot_points)

        return result

        
# This Code is Contributed by Kalyan Babu Allamudi