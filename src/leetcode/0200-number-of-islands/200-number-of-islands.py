class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        cnt = 0
        for rr, cc in product(range(len(grid)), range(len(grid[0]))):
            if grid[rr][cc] == '1':
                self.dfs(grid, rr, cc)
                cnt += 1
        return cnt

    def dfs(self, grid, r, c):
        grid[r][c] = 0
        for a, b in (1, 0), (-1, 0), (0, -1), (0, 1):
            rr, cc = r + a, c + b
            if 0 <= rr < len(grid) and 0 <= cc < len(grid[0]) and grid[rr][cc] == '1':
                self.dfs(grid, rr, cc)
