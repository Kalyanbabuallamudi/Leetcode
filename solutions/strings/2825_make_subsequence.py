class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        if len(str2) > len(str1):
            return False

        i, j = 0, 0

        while i < len(str1) and j < len(str2):
        
            next_char = chr(((ord(str1[i]) - ord('a') + 1) % 26) + ord('a'))
            if str1[i] == str2[j] or next_char == str2[j]:
                j += 1
            i += 1

        return j == len(str2)

# This code is contributed by Kalyan Babu Allamudi
