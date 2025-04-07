# 416. Partition Equal Subset Sum
from typing import List

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        # If total sum is odd, we cannot partition it equally
        if total % 2 != 0:
            return False

        target = total // 2
        n = len(nums)

        # dp[i] means whether a subset sum of 'i' is possible
        dp = [False] * (target + 1)
        dp[0] = True  # base case: sum 0 is always possible

        for num in nums:
            for i in range(target, num - 1, -1):
                dp[i] = dp[i] or dp[i - num]

        return dp[target]


# This Code is Contributed by Kalyan Babu Allamudi