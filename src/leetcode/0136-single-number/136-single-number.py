class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        """
        Topics: Array, Bit Manipulation
        """
        ans = 0
        for n in nums:
            ans ^= n

        return ans