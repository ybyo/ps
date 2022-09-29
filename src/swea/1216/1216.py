import sys

sys.stdin = open("input.txt", "r")


def pal_checker(s):
    for i in range(len(s) // 2):
        if s[i] != s[-i - 1]:
            return False
    return True


T = 10
for test_case in range(1, T + 1):
    N, M = int(input()), 100
    grid = [list(map(str, input())) for _ in range(M)]

    ans = 0

    for r in range(M):
        for c in range(M):
            tmp1, tmp2 = [], []
            for a in range(r, M):
                tmp1.append(grid[a][c])
                if len(tmp1) > ans and pal_checker(tmp1):
                    ans = max(ans, len(tmp1))
            for b in range(c, M):
                tmp2.append(grid[r][b])
                if len(tmp2) > ans and pal_checker(tmp2):
                    ans = max(ans, len(tmp2))

    print(f"#{test_case} {ans}")
