class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        n = len(nums)
        
        # Step 1: Apply operations
        for i in range(n - 1):
            if nums[i] == nums[i + 1]:
                nums[i] *= 2
                nums[i + 1] = 0
        
        # Step 2: Shift all 0's to the end
        result = [num for num in nums if num != 0]  # Keep all non-zero elements
        result.extend([0] * (n - len(result)))  # Append zeros
        
        return result


    # This Code is contributed by Kalyan Babu Allamudi