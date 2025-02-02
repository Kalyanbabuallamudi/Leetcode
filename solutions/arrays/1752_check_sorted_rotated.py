class Solution:
    def check(self, nums: List[int]) -> bool:
        # Count the number of "drops" in the array
        drop_count = 0
        n = len(nums)
        
        for i in range(n):
            if nums[i] > nums[(i + 1) % n]:
                drop_count += 1
                if drop_count > 1:
                    return False
        return True

# This code is Contributed by Kalyan Babu Allamudi