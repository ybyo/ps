import sys

sys.stdin = open("../1204/input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    n = N

    grid = [[i + 1 for i in range(N)] for _ in range(N)]
    val = N + 1
    r, c = 0, N - 1

    dirs = [(1, 0), (0, -1), (-1, 0), (0, 1)]
    dir_val = 0

    n -= 1
    while True:
        if val == N ** 2 + 1:
            break

        for _ in range(2):
            a, b = dirs[dir_val]
            for _ in range(n):
                r += a
                c += b
                grid[r][c] = val
                val += 1
            dir_val += 1
            dir_val = 0 if dir_val == 4 else dir_val
        n -= 1

    print(f"#{test_case}")
    for row in grid:
        print(' '.join(map(str, row)))
