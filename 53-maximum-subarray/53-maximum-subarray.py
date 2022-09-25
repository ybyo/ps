class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp = [0] * len(nums)
        
        for i in range(len(nums)):
            dp[i] = max(nums[i], dp[i - 1] + nums[i])

        return max(dp)
                
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = 10**4 * -1
        curr_sum = 0
        for n in nums:
            curr_sum = n + curr_sum
            if max_sum < curr_sum:
                max_sum = curr_sum
            if curr_sum <= 0:
                curr_sum = 0 

        return max_sum