class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 1
        
        longest = 1
        increasing = 1
        decreasing = 1
        
        for i in range(1, n):
            if nums[i] > nums[i - 1]:
                increasing += 1
                decreasing = 1
            elif nums[i] < nums[i - 1]:
                decreasing += 1
                increasing = 1
            else:
                increasing = 1
                decreasing = 1
            longest = max(longest, increasing, decreasing)
        
        return longest

# This Code is Contributed by Kalyan Babu Allamudi