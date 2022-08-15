class Solution:
    def solve(self, s: str, ops: dict) -> List[int]:
        if s.isdigit():
            return [int(s)]

        ans = []

        for i in range(len(s)):
            if s[i] in ops:
                lt = self.solve(s[:i], ops)
                rt = self.solve(s[i + 1:], ops)
                for a, b in product(lt, rt):
                    ans.append(ops[s[i]](a, b))

        return ans

    def diffWaysToCompute(self, s: str) -> List[int]:
        ops = {
            '+': lambda x, y: x + y,
            '-': lambda x, y: x - y,
            '*': lambda x, y: x * y,
        }

        return self.solve(s, ops)
