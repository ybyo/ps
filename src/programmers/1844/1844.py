# problem source: https://school.programmers.co.kr/learn/courses/30/lessons/1844

from collections import deque


def solution(maps):
    m, n = len(maps), len(maps[0])
    ans = set()
    dq = deque()

    dq.append((0, 0, 2))

    dirs = [-1, 0], [0, 1], [0, -1], [1, 0]

    while dq:
        r, c, cnt = dq.popleft()
        if r == m - 1 and c == n - 1:
            ans.add(cnt)

        k = 4
        for a, b in dirs:
            nr = a + r
            nc = b + c
            if 0 <= nr < m and 0 <= nc < n and maps[nr][nc] == 1:
                maps[nr][nc] = cnt + 1
                dq.append((nr, nc, cnt + 1))
            else:
                k -= 1
            if k == 0:
                ans.add(-1)

    return maps[m - 1][n - 1] - 1 if len(ans) > 1 else -1
