import heapq
from typing import List

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        # Convert nums into a min-heap
        heapq.heapify(nums)
        operations = 0
        
        while len(nums) > 1 and nums[0] < k:
            # Pop the two smallest elements
            x = heapq.heappop(nums)
            y = heapq.heappop(nums)
            
            # Perform the operation
            new_value = min(x, y) * 2 + max(x, y)
            heapq.heappush(nums, new_value)
            
            operations += 1
        
        # After the loop, if the smallest element is still < k, perform final operations
        return operations

# This Code is Contributed by Kalyan Babu Allamudi