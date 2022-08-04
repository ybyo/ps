class Solution:
    def longestSubsequence(self, s: str, k: int) -> int:
        nums = ''
        for i in range(len(s)-1, -1, -1):
            nums = s[i] + nums 
            if int(nums, base=2) > k:
                return s[:i].count('0') + len(nums) - 1
        return len(s)