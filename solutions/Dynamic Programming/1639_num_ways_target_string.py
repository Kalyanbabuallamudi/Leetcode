from typing import List
from collections import defaultdict

class Solution:
    def numWays(self, words: List[str], target: str) -> int:
        MOD = 10**9 + 7
        m, n = len(target), len(words[0])
        
        # Count frequency of each character at each column
        freq = [defaultdict(int) for _ in range(n)]
        for word in words:
            for i, ch in enumerate(word):
                freq[i][ch] += 1
        
        # Dynamic programming array: dp[j] = number of ways to form target[:j]
        dp = [0] * (m + 1)
        dp[0] = 1  # There's one way to form an empty target
        
        for i in range(n):
            for j in range(m, 0, -1):
                dp[j] += dp[j - 1] * freq[i].get(target[j - 1], 0)
                dp[j] %= MOD
        
        return dp[m]

# This Code is Contributed by Kalyan Babu Allamudi