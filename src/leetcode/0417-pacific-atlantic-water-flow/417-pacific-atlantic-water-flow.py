class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m, n = len(heights), len(heights[0])

        if m == 1 or n == 1:
            ans = []
            for r, c in product(range(m), range(n)):
                ans.append((r, c))
            return ans

        pac = [(0, p) for p in range(n)] + [(p, 0) for p in range(1, m)]
        atl = [(m - 1, a) for a in range(n)] + [(a, n - 1) for a in range(m - 1)]

        def bfs(dq):
            visited = set()
            dq = deque(dq)
            while dq:
                r, c = dq.popleft()
                visited.add((r, c))
                curr_h = heights[r][c]
                for nr, nc in map(lambda x: (x[0] + r, x[1] + c), [(1, 0), (-1, 0), (0, 1), (0, -1)]):
                    if 0 <= nr < m and 0 <= nc < n and (nr, nc) not in visited:
                        if heights[nr][nc] >= curr_h:
                            dq.append((nr, nc))
            return visited

        return bfs(pac) & bfs(atl)
