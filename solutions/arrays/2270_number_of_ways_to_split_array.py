class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        total_sum = sum(nums)
        left_sum = 0
        count = 0

        for i in range(len(nums) - 1):  # Ensure there is at least one element on the right
            left_sum += nums[i]
            right_sum = total_sum - left_sum
            if left_sum >= right_sum:
                count += 1

        return count

# This Code is Contributed by Kalyan Babu Allamudi