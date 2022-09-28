class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        candidates.sort()
        self.solve([], 0, candidates, target, ans)

        return ans

    def solve(self, ss, l, candidates, target, ans):
        if not target:
            ans.append(list(ss))
        
        if candidates[l] > target:
            return

        for i in range(l, len(candidates)):
            if candidates[i] > target:
                return
            ss.append(candidates[i])
            self.solve(ss, i, candidates, target - candidates[i], ans)
            ss.pop()
