from typing import List
import heapq

class Solution:
    def findScore(self, nums: List[int]) -> int:
        n = len(nums)
        marked = [False] * n  # Keeps track of whether each element is marked
        min_heap = [(num, i) for i, num in enumerate(nums)]  # Create a min-heap of (value, index) pairs
        heapq.heapify(min_heap)  # Convert list into a min-heap
        score = 0  # Initialize score
        
        while min_heap:
            value, index = heapq.heappop(min_heap)  # Get the smallest unmarked value
            if not marked[index]:  # Check if it's unmarked
                score += value  # Add its value to the score
                # Mark the element and its adjacent elements if they exist
                marked[index] = True
                if index > 0:  # Left adjacent element
                    marked[index - 1] = True
                if index < n - 1:  # Right adjacent element
                    marked[index + 1] = True

        return score

# This Code is Contributed by Kalyan Babu Allamudi