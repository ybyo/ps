# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        l_sum, r_sum = 0, sum(nums)
        for idx, piv in enumerate(nums):
            r_sum -= piv
            if l_sum == r_sum:
                return idx
            l_sum += piv
        return -1
# leetcode submit region end(Prohibit modification and deletion)
