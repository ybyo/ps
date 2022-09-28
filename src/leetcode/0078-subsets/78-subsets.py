class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def backtrack(curr, ss):
            ans.append(ss[:])

            for i in range(curr, len(nums)):
                ss.append(nums[i])
                backtrack(i + 1, ss)
                ss.pop()

        ans = []

        backtrack(0, [])

        return ans