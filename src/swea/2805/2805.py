import sys

sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    M = N // 2
    ans = 0

    grid = [list(map(int, input())) for _ in range(N)]
    k = 0
    for r in range(N):
        for c in range(N):
            if c == M:
                ans += sum(grid[r][c - k:c + k + 1])
        if r < M:
            k += 1
        else:
            k -= 1

    print(f"#{test_case} {ans}")
