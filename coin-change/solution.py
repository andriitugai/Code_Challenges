class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [0] + [amount + 1] * amount
        curr = 0

        while curr <= amount:
            for coin in coins:
                if coin <= curr:
                    dp[curr] = min(dp[curr - coin] + 1, dp[curr])

            curr += 1

        return dp[amount] if dp[amount] < amount + 1 else -1
