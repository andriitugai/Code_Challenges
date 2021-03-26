class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        num_days = len(prices)

        if num_days <= 1:
            return 0

        dp = [[0, 0]] * num_days
        dp[0][1] = -prices[0] - fee
        for i in range(1, num_days):
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i])
            dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] - prices[i] - fee)

        return dp[-1][0]
