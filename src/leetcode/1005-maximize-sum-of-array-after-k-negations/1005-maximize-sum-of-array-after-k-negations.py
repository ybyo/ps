from heapq import heapify, heapreplace

class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        heapify(nums)
        while k and nums[0] < 0:
            heapreplace(nums, -nums[0])
            k -= 1
        if k % 2:
            heapreplace(nums, -nums[0])
        return sum(nums)


class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        nums.sort()
        i = 0
        while i < len(nums) and k > 0 and nums[i] < 0:
            nums[i] = -nums[i]
            i += 1
            k -= 1
        return sum(nums) - k % 2 * min(nums) * 2
