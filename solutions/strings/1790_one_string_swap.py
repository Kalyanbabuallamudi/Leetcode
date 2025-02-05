class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if s1 == s2:
            return True
        
        # Find the indices where s1 and s2 differ
        diff = [(a, b) for a, b in zip(s1, s2) if a != b]
        
        # Check if there are exactly two differences and they can be swapped to make the strings equal
        return len(diff) == 2 and diff[0] == diff[1][::-1]

# This Code is Contributed by Kalyan Babu Allamudi