class Solution:
    def maximumGroups(self, grades: List[int]) -> int:
        ans, n = 0, len(grades)
        while n >= ans + 1:
            ans += 1
            n -= ans
        return ans
            