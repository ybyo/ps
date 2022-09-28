class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def bt(ss, vstd):
            if len(ss) == len(nums):
                ans.append(ss[:])
                return

            for i in range(len(nums)):
                if vstd[i]:
                    continue
                ss.append(nums[i])
                vstd[i] = True
                bt(ss, vstd)
                ss.pop()
                vstd[i] = False

        ans = []
        bt([], [False] * len(nums))
        
        return ans
