import sys

sys.stdin = open("input.txt", "r")

T = 10
for test_case in range(1, T + 1):
    _ = int(input())
    N = 100
    grid = [list(map(int, input().split())) for _ in range(N)]

    mskd = mmd = mhor = mver = 0

    for r in range(N):
        ver = hor = 0
        for c in range(N):
            if r == c:
                mmd += grid[r][c]
                mskd += grid[r][-c - 1]
            hor += grid[r][c]
            ver += grid[c][r]
        mhor = max(mhor, hor)
        mver = max(mver, ver)

    print(f"#{test_case} {max(mskd, mmd, mhor, mver)}")
