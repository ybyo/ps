class Solution:
    def isValid(self, s: str) -> bool:
        d = {'(': ')', '{': '}', '[': ']'}
        stk = []

        for c in s:
            if c in d:
                stk.append(c)
            elif not stk or d[stk.pop()] != c:
                return False

        return not stk
        
        