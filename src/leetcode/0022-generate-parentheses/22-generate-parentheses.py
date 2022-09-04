class Solution:
    @cache
    def generateParenthesis(self, n: int) -> List[str]:
        if n == 0:
            return ['']
        
        ans = []
        
        for i in range(n):
            for x in self.generateParenthesis(n - 1 - i): 
                for y in self.generateParenthesis(i): 
                    ans.append(f"({x}){y}")

        return ans 