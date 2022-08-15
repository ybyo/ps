class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        lt = rt = ldx = rdx = 0
        ss = []
        ans = ''
        for i, c in enumerate(s):
            if c == '(':
                lt += 1
            else:
                rt += 1
            if lt == rt:
                rdx = i
                ss.append(s[ldx:rdx + 1])
                ldx = rdx + 1
        
        for i in range(len(ss)):
            seg = ss[i][1:-1]
            ans += seg
        return ans