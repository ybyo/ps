class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stk = []
        s = list(s)
        
        for idx, c in enumerate(s):
            if c == '(':
                stk.append(idx)
            elif c == ')':
                if stk:
                    stk.pop()
                else:
                    s[idx] = ''

        for i in stk:
            s[i] = ''

        return ''.join(s)
