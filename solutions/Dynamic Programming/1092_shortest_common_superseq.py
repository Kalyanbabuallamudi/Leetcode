class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        # Helper function to compute the Longest Common Subsequence (LCS)
        def compute_lcs(s1, s2):
            m, n = len(s1), len(s2)
            dp = [[""] * (n + 1) for _ in range(m + 1)]
            
            for i in range(1, m + 1):
                for j in range(1, n + 1):
                    if s1[i - 1] == s2[j - 1]:
                        dp[i][j] = dp[i - 1][j - 1] + s1[i - 1]
                    else:
                        dp[i][j] = dp[i - 1][j] if len(dp[i - 1][j]) > len(dp[i][j - 1]) else dp[i][j - 1]
            return dp[m][n]
        
        # Compute the LCS of str1 and str2
        lcs = compute_lcs(str1, str2)
        
        # Construct the shortest common supersequence using LCS
        i, j = 0, 0
        result = []
        
        for char in lcs:
            while i < len(str1) and str1[i] != char:
                result.append(str1[i])
                i += 1
            while j < len(str2) and str2[j] != char:
                result.append(str2[j])
                j += 1
            result.append(char)
            i += 1
            j += 1
        
        result.extend(str1[i:])
        result.extend(str2[j:])
        
        return ''.join(result)
    
    # This Code is contributed by Kalyan Babu Allamudi