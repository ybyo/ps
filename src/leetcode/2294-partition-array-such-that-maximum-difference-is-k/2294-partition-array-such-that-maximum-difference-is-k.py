class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        nums.sort()
        ans = 1
        mn = mx = nums[0]
        for n in nums:
            mn, mx = min(mn, n), max(mx, n)
            if mx - mn > k:
                ans += 1
                mn = mx = n
        return ans