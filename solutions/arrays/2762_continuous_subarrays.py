from collections import deque

class Solution:
    def continuousSubarrays(self, nums: list[int]) -> int:
        n = len(nums)
        left = 0
        total_subarrays = 0
        
        # Deques to track the maximum and minimum in the current window
        max_deque = deque()
        min_deque = deque()
        
        for right in range(n):
            # Maintain max_deque for the max values in the sliding window
            while max_deque and nums[max_deque[-1]] <= nums[right]:
                max_deque.pop()
            max_deque.append(right)
            
            # Maintain min_deque for the min values in the sliding window
            while min_deque and nums[min_deque[-1]] >= nums[right]:
                min_deque.pop()
            min_deque.append(right)
            
            # If the max and min difference in the window exceeds 2, shift the window
            while nums[max_deque[0]] - nums[min_deque[0]] > 2:
                left += 1
                if max_deque[0] < left:
                    max_deque.popleft()
                if min_deque[0] < left:
                    min_deque.popleft()
            
            # Count all subarrays ending at 'right' and starting from 'left' to 'right'
            total_subarrays += (right - left + 1)
        
        return total_subarrays

# This Code is Contributed by Kalyan Babu Allamudi