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


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ans = 0
        m, n = len(grid), len(grid[0])

        def dfs(y, x):
            grid[y][x] = '0'
            for a, b in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nr = y + a
                nc = x + b
                if check(nr, nc) and grid[nr][nc] == '1':
                    dfs(nr, nc)

        def check(rr, cc):
            if 0 <= rr < m and 0 <= cc < n:
                return True
            return False

        for r, c in product(range(m), range(n)):
            if grid[r][c] == '1':
                dfs(r, c)
                ans += 1

        return ans
