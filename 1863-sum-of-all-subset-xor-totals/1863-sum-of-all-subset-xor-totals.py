class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        self.dfs(nums, 0, 0)
        
        return self.dfs(nums, 0, 0)
        
        
    def dfs(self, nums, idx, curr):
        if idx == len(nums):
            return curr
        
        with_curr = self.dfs(nums, idx + 1, curr ^ nums[idx])
        without_curr = self.dfs(nums, idx + 1, curr)
        
        return with_curr + without_curr