class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp = [0] * len(nums)
        
        for i in range(len(nums)):
            dp[i] = max(nums[i], dp[i - 1] + nums[i])

        return max(dp)
                
            