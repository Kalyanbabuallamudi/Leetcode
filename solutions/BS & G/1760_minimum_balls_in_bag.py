from typing import List

class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        def can_divide(max_balls: int) -> bool:
            
            operations = 0
            for balls in nums:
                if balls > max_balls:
                
                    operations += (balls - 1) // max_balls  
            return operations <= maxOperations
        
        
        low, high = 1, max(nums)
        result = high
        
        while low <= high:
            mid = (low + high) // 2
            if can_divide(mid):
                result = mid
                high = mid - 1  
            else:
                low = mid + 1  
        return result
