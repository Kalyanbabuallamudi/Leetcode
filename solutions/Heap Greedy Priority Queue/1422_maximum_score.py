class Solution:
    def maxScore(self, s: str) -> int:
        # Initialize variables
        max_score = 0
        
        # Iterate through possible split points
        for i in range(1, len(s)):
            # Calculate the score for this split
            left_score = s[:i].count('0')
            right_score = s[i:].count('1')
            max_score = max(max_score, left_score + right_score)
        
        return max_score

# This Code is Contributed by Kalyan Babu Allamudi