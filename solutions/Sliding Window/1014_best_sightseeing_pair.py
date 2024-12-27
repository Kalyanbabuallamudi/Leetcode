from typing import List

class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        max_score = 0
        max_i_value = values[0]  # Initialize with values[0] + 0
        
        for j in range(1, len(values)):
            # Calculate the score for the current pair
            max_score = max(max_score, max_i_value + values[j] - j)
            # Update max_i_value for the next iteration
            max_i_value = max(max_i_value, values[j] + j)
        
        return max_score


# This Code is Contributed by Kalyan Babu Allamudi