class Solution:
    def constructDistancedSequence(self, n: int) -> list[int]:
        def backtrack(index):
            if index == 2 * n - 1:  # Base case: all indices are filled
                return True
            if result[index] != 0:  # Skip already filled indices
                return backtrack(index + 1)
            for num in range(n, 0, -1):  # Try larger numbers first
                if used[num]:
                    continue
                if num == 1 or (index + num < len(result) and result[index + num] == 0):
                    result[index] = num
                    if num > 1:
                        result[index + num] = num
                    used[num] = True
                    if backtrack(index + 1):  # Recurse to next index
                        return True
                    result[index] = 0
                    if num > 1:
                        result[index + num] = 0
                    used[num] = False
            return False

        result = [0] * (2 * n - 1)
        used = [False] * (n + 1)
        backtrack(0)
        return result

# This Code is Contributed by Kalyan Babu Allamudi