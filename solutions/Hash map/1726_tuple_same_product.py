from collections import defaultdict

class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        product_map = defaultdict(int)
        result = 0

        # Iterate over all pairs of numbers
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                product = nums[i] * nums[j]
                result += 8 * product_map[product]
                product_map[product] += 1

        return result

# This code is Contributed by Kalyan Babu Allamudi