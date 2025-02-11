class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        while part in s:
            s = s.replace(part, "", 1)  # Remove the leftmost occurrence of `part`
        return s

# This code is Contributed by Kalyan Babu Allamudi