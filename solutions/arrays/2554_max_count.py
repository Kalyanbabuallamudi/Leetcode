class Solution:
    def maxCount(self, banned: list[int], n: int, maxSum: int) -> int:
        banned_set = set (banned)
        chosen_sum = 0
        count = 0
        for i in range(1, n+1):
            if i not in banned_set and chosen_sum + i <= maxSum:
                chosen_sum += i
                count += 1
        return count
    
#This code is Contributed by Kalyan Babu Allamudi
