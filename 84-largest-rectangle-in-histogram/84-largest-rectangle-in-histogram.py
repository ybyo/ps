class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights.append(0)
        s = [0]
        ans = heights[0]
        for i in range(1, len(heights)):
            while s and heights[s[-1]] > heights[i]:
                h = heights[s.pop()]
                rb = s[-1] if s else -1
                w = i - rb - 1
                ans = max(ans, w * h)

            s.append(i)

        return ans