class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        """
        Category: Math, Dynamic Programming, Combinatorics
        """
        
        dp = [[1] * n] * m

        for r, c in product(range(1, m), range(1, n)):
                dp[r][c] = dp[r - 1][c] + dp[r][c - 1]

        return dp[-1][-1]