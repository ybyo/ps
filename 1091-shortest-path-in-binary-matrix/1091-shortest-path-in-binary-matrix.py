class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        
        if grid[0][0] or grid[n - 1][n - 1]:
            return -1
        
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1), (-1, -1), (1, 1), (1, -1),(-1, 1)]
        visited = set()
        q = deque([(0, 0, 1)])
        visited.add((0, 0))

        while q:
            r, c, cnt = q.popleft()
            if r == n - 1 and c == n - 1:
                return cnt
            for a, b in dirs:
                rr, cc = r + a, c + b
                if 0 <= rr < n and 0 <= cc < n:
                    if (rr, cc) not in visited and not grid[rr][cc]:
                        visited.add((rr, cc))
                        q.append((rr, cc, cnt + 1))
        return -1
