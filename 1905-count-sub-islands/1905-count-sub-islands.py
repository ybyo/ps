class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        m, n = len(grid2), len(grid2[0])
        ans = 0

        def dfs(r, c):
            if not (0 <= r < m and 0 <= c < n and grid2[r][c] == 1):
                return
            grid2[r][c] = 0
            dfs(r - 1, c)
            dfs(r + 1, c)
            dfs(r, c - 1)
            dfs(r, c + 1)

        for r, c in product(range(m), range(n)):
            if grid2[r][c] == 1 and grid1[r][c] == 0:
                dfs(r, c)

        for r, c in product(range(m), range(n)):
            if grid2[r][c] == 1:
                ans += 1
                dfs(r, c)

        return ans
