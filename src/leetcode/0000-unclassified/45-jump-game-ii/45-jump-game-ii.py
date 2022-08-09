class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) == 1: 
            return 0
        jump_min = jump_max = ans = 0
        while jump_max < len(nums) - 1:
            ans += 1
            nxt_max = max([i + nums[i] for i in range(jump_min, jump_max+1)])
            jump_min, jump_max = jump_max + 1, nxt_max
        return ans