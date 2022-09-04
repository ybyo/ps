class Solution:
    def climbStairs(self, n: int) -> int:
        memo = [None] * 45
        
        memo[0] = 1
        memo[1] = 2
        
        for i in range(2, 45):
            memo[i] = memo[i - 1] + memo[i - 2]
            
        
        return memo[n - 1]