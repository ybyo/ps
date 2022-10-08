class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        
        N = amount + 1
        dp = [N] * N
        dp[0] = 0
        
        for i in range(1, N):
            for coin in coins:
                if i - coin >= 0:
                    dp[i] = min(dp[i], dp[i - coin] + 1)
                
        return dp[N - 1] if dp[N - 1] < N else -1
        