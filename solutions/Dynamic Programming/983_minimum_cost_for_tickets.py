class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        day_set = set(days)  # For quick lookup of travel days
        last_day = days[-1]
        dp = [0] * (last_day + 1)

        for i in range(1, last_day + 1):
            if i not in day_set:
                dp[i] = dp[i - 1]  # No travel on this day, cost remains the same
            else:
                dp[i] = min(
                    dp[i - 1] + costs[0],  # 1-day pass
                    dp[i - 7] + costs[1] if i >= 7 else costs[1],  # 7-day pass
                    dp[i - 30] + costs[2] if i >= 30 else costs[2]  # 30-day pass
                )
        return dp[last_day]


# This Code is contributed by Kalyan Babu Allamudi