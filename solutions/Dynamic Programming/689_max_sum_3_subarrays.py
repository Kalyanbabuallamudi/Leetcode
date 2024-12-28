from typing import List

class Solution:
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        # Calculate the sums of all subarrays of length k
        n = len(nums)
        window_sum = [0] * (n - k + 1)
        curr_sum = sum(nums[:k])
        window_sum[0] = curr_sum
        
        for i in range(1, len(window_sum)):
            curr_sum += nums[i + k - 1] - nums[i - 1]
            window_sum[i] = curr_sum
        
        # Left and right indices for maximum sums
        left = [0] * len(window_sum)
        right = [0] * len(window_sum)
        
        # Fill left max sum indices
        max_idx = 0
        for i in range(len(window_sum)):
            if window_sum[i] > window_sum[max_idx]:
                max_idx = i
            left[i] = max_idx
        
        # Fill right max sum indices
        max_idx = len(window_sum) - 1
        for i in range(len(window_sum) - 1, -1, -1):
            if window_sum[i] >= window_sum[max_idx]:  # Use >= to prefer smaller index
                max_idx = i
            right[i] = max_idx
        
        # Find the max sum using left, middle, and right
        max_sum = 0
        result = []
        for j in range(k, len(window_sum) - k):
            l, r = left[j - k], right[j + k]
            curr_sum = window_sum[l] + window_sum[j] + window_sum[r]
            if curr_sum > max_sum:
                max_sum = curr_sum
                result = [l, j, r]
        
        return result


# This Code is Contributed by Kalyan Babu Allamudi