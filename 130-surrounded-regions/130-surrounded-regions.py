class Solution:
    def solve(self, board: List[List[str]]) -> None:
        m, n = len(board), len(board[0])
        if m <= 2 or n <= 2:
            return
        dq = deque()
        for r in range(m):
            dq.extend([(r, 0), (r, n - 1)])
        for c in range(n):
            dq.extend([(0, c), (m - 1, c)])
        while dq:
            r, c = dq.popleft()
            if 0 <= r < m and 0 <= c < n and board[r][c] == 'O':
                board[r][c] = '.'
                dq.extend([(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)])
        for r, c in product(range(m), range(n)):
                if board[r][c] == '.':
                    board[r][c] = 'O'
                else:
                    board[r][c] = 'X'
