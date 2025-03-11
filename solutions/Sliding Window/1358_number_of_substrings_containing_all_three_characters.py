class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        count = {'a': 0, 'b': 0, 'c': 0}
        left = 0
        result = 0

        for right in range(len(s)):
            count[s[right]] += 1

            # Check if all characters 'a', 'b', and 'c' are present in the current window
            while all(count[char] > 0 for char in 'abc'):
                result += len(s) - right  # All substrings from the current left to the end of the string are valid
                count[s[left]] -= 1
                left += 1

        return result


# This Code is Contributed by Kalyan Babu Allamudi