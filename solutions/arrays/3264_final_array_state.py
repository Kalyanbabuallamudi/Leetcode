class Solution:
    def getFinalState(self, nums: list[int], k:int, multiplier: int) -> list[int]:
        for _ in range(k):
            min_index = nums.index(min(nums))
            nums[min_index] *= multiplier
        return nums
    
# This Code is Contributed by Kalyan Babu Allamudi