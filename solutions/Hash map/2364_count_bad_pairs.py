from collections import defaultdict
from typing import List

class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        n = len(nums)
        total_pairs = n * (n - 1) // 2
        count_map = defaultdict(int)
        good_pairs = 0
        
        for i, num in enumerate(nums):
            diff = num - i
            good_pairs += count_map[diff]
            count_map[diff] += 1
        
        bad_pairs = total_pairs - good_pairs
        return bad_pairs

# This code is Contributed by Kalyan Babu Allamudi