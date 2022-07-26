class Solution:
    def makeGood(self, s: str) -> str:
        stk = []        
        for c in s:
            if stk and stk[-1] == c.swapcase():
                stk.pop()
            else:
                stk.append(c)
                
        return ''.join(stk)