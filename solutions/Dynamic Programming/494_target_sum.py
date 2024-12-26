from typing import List

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        total_sum = sum(nums)
        
        # If the target is out of the range of possible sums, return 0
        if total_sum < abs(target) or (total_sum + target) % 2 != 0:
            return 0
        
        subset_sum = (total_sum + target) // 2
        
        # DP array to store the number of ways to achieve each sum
        dp = [0] * (subset_sum + 1)
        dp[0] = 1  # There's one way to get sum 0: use no elements
        
        for num in nums:
            for j in range(subset_sum, num - 1, -1):
                dp[j] += dp[j - num]
        
        return dp[subset_sum]


# This code is Contributed by Kalyan Babu Allamudi