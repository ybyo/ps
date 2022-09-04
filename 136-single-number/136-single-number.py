class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        """
        Category: Array, Bit Manipulation
        """
        if len(nums) == 1:
            return nums[0]
        
        d = Counter(nums)
        nums = set(nums)
        
        for n in nums:
            if d[n] == 1:
                return n
