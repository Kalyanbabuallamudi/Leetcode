from typing import List
class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        seen = set ()
        for num in arr:
            if 2 * num in seen or (num % 2 == 0 and num // 2 in seen):
                return True
            seen.add(num)
        return False

solution = Solution()
print(solution.checkIfExist([10, 2, 5, 3])) #Output: True
print(solution.checkIfExist([3, 1, 7, 11])) #Output: False

# This code is contributed by Kalyan Babu Allamudi