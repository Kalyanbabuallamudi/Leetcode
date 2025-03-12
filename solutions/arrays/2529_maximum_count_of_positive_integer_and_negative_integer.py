class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        # Count positive and negative numbers
        pos_count = 0
        neg_count = 0

        for num in nums:
            if num > 0:
                pos_count += 1
            elif num < 0:
                neg_count += 1

        # Return the maximum of the two counts
        return max(pos_count, neg_count)


# This Code is Contributed by Kalyan Babu Allamudi