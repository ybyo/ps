class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        ans = 0
        m, n = len(grid), len(grid[0])

        def dfs(r, c):
            if not 0 <= r < m or not 0 <= c < n:
                return False
            if grid[r][c] != 0:
                return True
            grid[r][c] = -1
            
            return all([dfs(r - 1, c),
                        dfs(r + 1, c),
                        dfs(r, c - 1),
                        dfs(r, c + 1)])

        for r, c in product(range(m), range(n)):
            if grid[r][c] == 0 and dfs(r, c):
                ans += 1

        return ans