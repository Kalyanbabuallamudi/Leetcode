class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        MOD = 10**9 + 7
        dp = [0] * (high + 1)
        dp[0] = 1  # Base case: one way to form an empty string

        # Iterate through all possible string lengths up to `high`
        for length in range(1, high + 1):
            if length >= zero:
                dp[length] += dp[length - zero]
            if length >= one:
                dp[length] += dp[length - one]
            dp[length] %= MOD

        # Sum up all counts for lengths between `low` and `high`
        return sum(dp[low:high + 1]) % MOD

# This Code is Contributed by Kalyan Babu Allamudi