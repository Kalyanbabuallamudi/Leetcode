class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        def can_distribute(mid: int) -> bool:
            # Check if we can allocate `mid` candies to each child
            total = sum(candy // mid for candy in candies)
            return total >= k

        if sum(candies) < k:
            return 0  # Not enough candies for all children

        low, high = 1, max(candies)
        result = 0

        while low <= high:
            mid = (low + high) // 2
            if can_distribute(mid):
                result = mid
                low = mid + 1  # Try for a larger number
            else:
                high = mid - 1  # Try for a smaller number

        return result



# This Code is Contributed by Kalyan Babu Allamudi