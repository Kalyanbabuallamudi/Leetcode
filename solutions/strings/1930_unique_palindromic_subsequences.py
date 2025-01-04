class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        from collections import defaultdict

        # Initialize variables
        first_occurrence = {}
        last_occurrence = {}
        unique_palindromes = set()

        # Record the first and last occurrences of each character
        for i, char in enumerate(s):
            if char not in first_occurrence:
                first_occurrence[char] = i
            last_occurrence[char] = i

        # Iterate through all characters in first_occurrence
        for char in first_occurrence:
            start, end = first_occurrence[char], last_occurrence[char]
            if end - start > 1:  # Ensure there is a range for middle characters
                # Collect middle characters between the first and last occurrence
                middle_chars = set(s[start + 1:end])
                # Add all palindromic sequences to the set
                for mid_char in middle_chars:
                    unique_palindromes.add((char, mid_char, char))

        # Return the count of unique palindromic subsequences
        return len(unique_palindromes)

# This Code is Contributed by Kalyan Babu Allamudi