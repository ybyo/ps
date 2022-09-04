class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        """
        Topics: Array, Hash Table, Divide and Coquer, Sorting, Counting
        """     
        nums.sort()
        
        return nums[len(nums) // 2]
        