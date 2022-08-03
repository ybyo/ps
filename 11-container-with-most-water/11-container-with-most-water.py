class Solution:
    def maxArea(self, height: List[int]) -> int:
        lt, rt = 0, len(height) - 1
        ans = 0
        while lt < rt:
            ans = max(ans, min(height[lt], height[rt]) * (rt-lt))
            if height[lt] < height[rt]:
                lt += 1
            else:
                rt -= 1
        return ans
        