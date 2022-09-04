class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights.append(0)
        stk = [0]
        ans = heights[0]

        for i in range(1, len(heights)):
            while stk and heights[stk[-1]] > heights[i]:
                h = heights[stk.pop()]
                rb = stk[-1] if stk else -1
                w = i - rb - 1
                ans = max(ans, w * h)

            stk.append(i)

        return ans