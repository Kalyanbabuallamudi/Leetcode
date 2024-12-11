from collections import Counter

class Solution:
    def maximumBeauty(self, nums: list[int], k: int) -> int:
        # Step 1: Reduce the range of each element to [num - k, num + k]
        reduced_ranges = [(num - k, num + k) for num in nums]
        
        # Step 2: Use a Counter to track entry and exit points of the ranges
        counter = Counter()
        for start, end in reduced_ranges:
            counter[start] += 1  # Increment at the start of the range
            counter[end + 1] -= 1  # Decrement after the end of the range
        
        # Step 3: Calculate the maximum beauty using a running sum of active intervals
        max_beauty = 0
        current_beauty = 0
        for point in sorted(counter):
            current_beauty += counter[point]
            max_beauty = max(max_beauty, current_beauty)
        
        return max_beauty
# This code is Contributed by Kalyan Babu Allamudi