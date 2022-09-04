class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        ans, cnt = [], 0
        
        for c in s:
            if c == '(' and cnt > 0:
                ans.append(c)
            if c == ')' and cnt > 1:
                ans.append(c)
            cnt += 1 if c == '(' else -1

        return ''.join(ans)