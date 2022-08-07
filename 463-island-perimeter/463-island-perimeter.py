class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        ans = 0
        for r, c in product(range(m), range(n)):
            if grid[r][c] == 1:
                ans += 4
                if r and grid[r-1][c] == 1:
                    ans -= 2
                if c and grid[r][c-1] == 1:
                    ans -= 2
        return ans