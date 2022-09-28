class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        """
        Topics: Array, DFS, BFS, Union-find, Matrix
        """
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
        