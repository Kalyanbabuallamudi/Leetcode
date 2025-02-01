class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        # Iterate through the array and check adjacent elements
        for i in range(len(nums) - 1):
            if nums[i] % 2 == nums[i + 1] % 2:
                return False
        return True

# This code is contributed by Kalyan Babu Allamudi