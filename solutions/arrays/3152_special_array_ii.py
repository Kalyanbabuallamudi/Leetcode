from typing import List

class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        
       
        n = len(nums)
        
        
        parity = [0] * (n - 1)
        for i in range(n - 1):
            if (nums[i] % 2) != (nums[i + 1] % 2):
                parity[i] = 1
        
        
        prefix_sum = [0] * n
        for i in range(1, n):
            prefix_sum[i] = prefix_sum[i - 1] + parity[i - 1]
        
        result = []
        for fromi, toi in queries:
            
            if fromi == toi:
                result.append(True)
            else:
                
                total_changes = prefix_sum[toi] - prefix_sum[fromi]
               
                result.append(total_changes == (toi - fromi))
        
        return result
