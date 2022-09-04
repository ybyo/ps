class Solution:
    def diffWaysToCompute(self, s: str) -> List[int]:
        self.memo = defaultdict(list)
        
        return self.solve(s)

    def solve(self, s: str) -> List[int]:
        if s in self.memo:
            return self.memo[s]

        if s.isdigit():
            return [int(s)]
        
        ans = []
        
        ops = {
            '+': lambda x, y: x + y,
            '-': lambda x, y: x - y,
            '*': lambda x, y: x * y,
        }

        for i in range(len(s)):
            if s[i] in ops:
                lt = self.solve(s[:i])
                rt = self.solve(s[i + 1:])
                for a, b in product(lt, rt):
                    ans.append(ops[s[i]](a, b))

        return ans
