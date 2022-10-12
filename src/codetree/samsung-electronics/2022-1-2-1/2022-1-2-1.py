import sys

sys.stdin = open("input.txt", "r")

# problem source: https://www.codetree.ai/frequent-problems/tail-catch-play/description

N, M, K = map(int, input().split())

grid = [list(map(int, input().split())) for _ in range(N)]
dirs = [1, 0], [-1, 0], [0, 1], [0, -1]
trains = [[] for _ in range(M)]
roads = [[] for _ in range(M)]
counted = []

global ans
ans = 0


def pp(grid):
    for row in grid:
        print(row)
    print()


def border_check(r, c):
    return 0 <= r < N and 0 <= c < N


def find_train():
    i = 0
    for r in range(N):
        for c in range(N):
            if grid[r][c] == 1 and (r, c) not in counted:
                trains[i].append((r, c))
                i += 1

    for i in range(M):
        r, c = trains[i][0]
        chaining(i, r, c, False)


def chaining(i, r, c, found_tail):
    counted.append((r, c))
    for a, b in dirs:
        nr = r + a
        nc = c + b
        if not border_check(nr, nc) or (nr, nc) in counted:
            continue
        if not found_tail:
            if grid[nr][nc] == 2:
                trains[i].append((nr, nc))
                counted.append((nr, nc))
                chaining(i, nr, nc, False)
            elif len(trains[i]) >= 2 and grid[nr][nc] == 3:
                trains[i].append((nr, nc))
                counted.append((nr, nc))
                chaining(i, nr, nc, True)
        else:
            if grid[nr][nc] == 4:
                roads[i].append((nr, nc))
                counted.append((nr, nc))
                chaining(i, nr, nc, True)


def move():
    for i in range(M):
        if not roads[i]:
            next_road = trains[i][-1]
            trains[i].insert(0, next_road)
            trains[i].pop()
            continue
        next_road = roads[i][-1]
        tail = trains[i][-1]
        trains[i].insert(0, next_road)
        roads[i].insert(0, tail)
        trains[i].pop()
        roads[i].pop()


def throw_ball(n):
    k = n % N
    d = (n // N) % 4

    if d == 0:
        for i in range(N):
            ball_pos = (k, i)
            for j in range(M):
                if ball_pos in trains[j]:
                    return ball_pos, j
    elif d == 1:
        for i in range(N - 1, -1, -1):
            ball_pos = (i, k)
            for j in range(M):
                if ball_pos in trains[j]:
                    return ball_pos, j
    elif d == 2:
        for i in range(N - 1, -1, -1):
            ball_pos = (N - 1 - k, i)
            for j in range(M):
                if ball_pos in trains[j]:
                    return ball_pos, j
    else:
        for i in range(N):
            ball_pos = (i, N - 1 - k)
            for j in range(M):
                if ball_pos in trains[j]:
                    return ball_pos, j

    return (-1, -1), -1


def get_point(ball_pos, idx):
    global ans
    pts = trains[idx].index(ball_pos) + 1
    ans += pts ** 2


def swap_head(idx):
    trains[idx].reverse()
    roads[idx].reverse()


find_train()
del counted[:]

for k in range(K):
    move()
    ball_pos, idx = throw_ball(k)
    if ball_pos != (-1, -1):
        get_point(ball_pos, idx)
        swap_head(idx)

print(ans)
