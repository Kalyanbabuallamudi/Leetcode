from typing import List
class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        n = len(prices)
        result = prices[:]  # Copy prices to result array
        
        # Loop through each price
        for i in range(n):
            for j in range(i + 1, n):
                if prices[j] <= prices[i]:
                    result[i] -= prices[j]
                    break  # Stop at the first discount found
        
        return result

# This code is Contributed by Kalyan Babu Allamudi