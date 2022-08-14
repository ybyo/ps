class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        p = ''
        lt = rt = 0
        
        def solve(p, lt, rt):
            if len(p) == 2 * n:
                ans.append(p)
                return 
            if lt < n:
                p += '('
                solve(p, lt + 1, rt)
                p = p[:-1]
            if rt < lt:
                p += ')'
                solve(p, lt, rt + 1)
                p = p[:-1]

        solve(p, lt, rt)
        
        return ans
        
            