import sys

sys.stdin = open("input.txt", "r")


def dfs(r, c, k, cnt):
    global ans
    ans = max(ans, cnt)

    for a, b in dirs:
        nr, nc = r + a, c + b
        if not (0 <= nr < N and 0 <= nc < N and not vstd[nr][nc]):
            continue
        if grid[r][c] > grid[nr][nc]:
            vstd[nr][nc] = True
            dfs(nr, nc, k, cnt + 1)
            vstd[nr][nc] = False
        else:
            t = grid[nr][nc] - grid[r][c]
            if k and t + 1 <= k:
                vstd[nr][nc] = True
                grid[nr][nc] -= t + 1
                dfs(nr, nc, -1, cnt + 1)
                vstd[nr][nc] = False
                grid[nr][nc] += t + 1


T = int(input())
for test_case in range(1, T + 1):
    N, K = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(N)]
    vstd = [[False] * N for _ in range(N)]
    M = max(map(max, grid))
    coord = []
    ans = 0

    for r in range(N):
        for c in range(N):
            if grid[r][c] == M:
                coord.append([r, c])

    dirs = [1, 0], [-1, 0], [0, 1], [0, -1]

    for r, c in coord:
        vstd[r][c] = True
        dfs(r, c, K, 1)
        vstd[r][c] = False

    print(f"#{test_case} {ans}")
