class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtrack(ss, rem, curr, ans):
            if rem == 0:
                ans.append(list(ss))
                return
            for i in range(curr, len(candidates)):
                if i > curr and candidates[i] == candidates[i - 1]:
                    continue
                if rem < candidates[i]:
                    break
                ss.append(candidates[i])
                backtrack(ss, rem - candidates[i], i + 1, ans)
                ss.pop()

        candidates.sort()
        ss, ans = [], []
        backtrack(ss, target, 0, ans)

        return ans
