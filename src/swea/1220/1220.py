import sys
from collections import deque

sys.stdin = open("input.txt", "r")

T = 10
for test_case in range(1, T + 1):
    N = int(input())
    grid = [list(map(int, input().split())) for _ in range(N)]
    ans = 0

    for c in range(N):
        cnt, dq = 0, deque()
        for r in range(N):
            magnet = grid[r][c]
            if not dq:
                if magnet == 1:
                    dq.append(magnet)
            else:
                if magnet != 0:
                    if dq[-1] != magnet:
                        dq.append(magnet)
        ans += len(dq) // 2

    print(f"#{test_case} {ans}")
