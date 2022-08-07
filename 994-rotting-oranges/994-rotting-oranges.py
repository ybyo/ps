class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        fresh = time_passed = 0
        dq = deque()
        for r, c in product(range(m), range(n)):
            if grid[r][c] == 2:
                dq.append((r, c))
            if grid[r][c] == 1:
                fresh += 1
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        while dq and fresh:
            time_passed += 1
            for _ in range(len(dq)):
                y, x = dq.popleft()
                for dy, dx in dirs:
                    if 0 <= y + dy < m and 0 <= x + dx < n and grid[y + dy][x + dx] == 1:
                        fresh -= 1
                        grid[y + dy][x + dx] = 2
                        dq.append((y + dy, x + dx))
        return time_passed if fresh == 0 else -1
