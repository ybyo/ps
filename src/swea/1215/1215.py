import sys

sys.stdin = open("input.txt", "r")


def pal_checker(s):
    for i in range(len(s) // 2):
        if s[i] != s[-i - 1]:
            return False
    return True


T = 10
for test_case in range(1, T + 1):
    N, M = int(input()), 8
    grid = [list(map(str, input())) for _ in range(8)]
    ans = 0
    lists = []
    for r in range(M):
        for c in range(M):
            if c + N <= M:
                h = grid[r][c:c + N]
                if pal_checker(h):
                    ans += 1
            if r + N <= M:
                v = []
                for a in range(r, r + N):
                    v.append(grid[a][c])
                if pal_checker(v):
                    ans += 1

    print(f"#{test_case}, {ans}")
