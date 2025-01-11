from collections import Counter

class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        # If k is greater than the length of the string, it's not possible to form k palindromes
        if k > len(s):
            return False
        
        # Count the frequency of each character
        freq = Counter(s)
        
        # Count the number of characters with odd frequencies
        odd_count = sum(1 for count in freq.values() if count % 2 != 0)
        
        # To form k palindromes, we need at least odd_count <= k
        return odd_count <= k

# This Code is Contributed by Kalyan Babu Allamudi