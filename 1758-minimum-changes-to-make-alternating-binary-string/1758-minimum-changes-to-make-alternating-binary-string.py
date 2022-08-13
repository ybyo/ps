class Solution:
    def minOperations(self, s: str) -> int:
        ans = 0
        s = list(s)
        
        for i in range(0, len(s) - 1):
            if s[i] == s[i + 1]:
                ans += 1
                if s[i] == '0':
                    s[i + 1] = '1'
                else:
                    s[i + 1] = '0'
                    
        return min(ans, len(s) - ans)