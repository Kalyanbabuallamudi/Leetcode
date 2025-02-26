from typing import List

class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        max_sum = 0
        min_sum = 0
        current_sum = 0

        for num in nums:
            current_sum += num
            max_sum = max(max_sum, current_sum)
            min_sum = min(min_sum, current_sum)
        
        return max_sum - min_sum
    

# This Code is Contributed by Kalyan Babu Allamudi