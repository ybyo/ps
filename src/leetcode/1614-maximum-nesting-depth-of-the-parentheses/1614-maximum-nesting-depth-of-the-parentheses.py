class Solution:
    def maxDepth(self, s: str) -> int:
        ans = cnt = 0

        for c in s:
            if c == '(':
                cnt += 1
            elif c == ')':
                ans = max(ans, cnt)
                cnt -= 1

        return ans
        