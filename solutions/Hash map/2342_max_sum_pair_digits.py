from collections import defaultdict
from typing import List

class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        def digit_sum(num: int) -> int:
            return sum(int(d) for d in str(num))
        
        digit_sum_map = defaultdict(list)
        max_sum = -1
        
        for num in nums:
            d_sum = digit_sum(num)
            if digit_sum_map[d_sum]:
                max_sum = max(max_sum, num + max(digit_sum_map[d_sum]))
            digit_sum_map[d_sum].append(num)
        
        return max_sum

# This code is Contributed by Kalyan Babu Allamudi