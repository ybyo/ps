class Solution:
    def diffWaysToCompute(self, s: str) -> List[int]:
        ans = []
        
        ops = {
            '+': lambda x, y: x + y,
            '-': lambda x, y: x - y,
            '*': lambda x, y: x * y,
        }
        
        if s.isdigit():
            return [int(s)]

        for i in range(len(s)):
            if s[i] in ops:
                lt = self.diffWaysToCompute(s[:i])
                rt = self.diffWaysToCompute(s[i + 1:])
                for a, b in product(lt, rt):
                    ans.append(ops[s[i]](a, b))

        return ans
