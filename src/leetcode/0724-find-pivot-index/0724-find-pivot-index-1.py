# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        l_sum = 0
        r_sum = 0
        for num in nums:
            r_sum += num
        r_sum -= nums[0]
        piv = 0
        while piv < len(nums):
            if l_sum == r_sum:
                return piv
            l_sum += nums[piv]
            piv += 1
            r_sum -= nums[piv]
        return -1
# leetcode submit region end(Prohibit modification and deletion)
