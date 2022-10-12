import sys

sys.stdin = open("input.txt", "r")


# problem source: https://www.codetree.ai/frequent-problems/tree-kill-all/description

def pp(grid):
    for row in grid:
        print(row)
    print()
    return


def border_check(r, c):
    return 0 <= r < N and 0 <= c < N


# 성장
# 성장은 모든 나무 동시에(deepcopy)
# 주변에 나무가 있는 칸의 수 만큼 증가
def grow_tree():
    after_grow = [row[:] for row in grid]
    lists = []
    for r in range(N):
        for c in range(N):
            if grid[r][c] > 0:
                lists.append((r, c))
    for r, c in lists:
        for a, b in dirs:
            nr = r + a
            nc = c + b
            if border_check(nr, nc) and grid[nr][nc] > 0:
                after_grow[nr][nc] += 1

    return [row[:] for row in after_grow]


# 번식
# 모든 나무 동시에(deepcopy)
# 기존 나무 대상 인접한 4개의 칸에 "벽 + 다른 나무 + 제초제 모두 없는 칸"에 번식
# 번식양: 번식 가능한 칸의 갯수만큼 나눈 수를 더함(나머지 버림)
def spread():
    after_spread = [row[:] for row in grid]
    lists = []
    for r in range(N):
        for c in range(N):
            if grid[r][c] > 0:
                cnt = 0
                tmp = []
                for a, b in dirs:
                    nr = a + r
                    nc = b + c
                    if border_check(nr, nc) and herbi_grid[nr][nc] == 0 and grid[nr][nc] == 0:
                        tmp.append([nr, nc])
                        cnt += 1
                lists.append([r, c, cnt, tmp])

    for l in lists:
        r, c = l[0], l[1]
        cnt = l[2]
        for k in range(cnt):
            nr, nc = l[3][k][0], l[3][k][1]
            if cnt > 0:
                after_spread[nr][nc] += grid[r][c] // cnt

    return [row[:] for row in after_spread]


# 제초 위치 찾기
def find_coord():
    max_val = 0
    _r, _c = -10, -10
    for r in range(N - 1, -1, -1):
        for c in range(N - 1, -1, -1):
            cnt = 0
            if grid[r][c] <= 0:
                cnt += grid[r][c]
                if cnt >= max_val:
                    max_val = cnt
                    _r, _c = r, c
            if grid[r][c] > 0:
                cnt += grid[r][c]
                for a, b in ddirs:
                    for i in range(1, K + 1):
                        nr = r + a * i
                        nc = c + b * i
                        if border_check(nr, nc):
                            if grid[nr][nc] <= 0:
                                break
                            else:
                                cnt += grid[nr][nc]
                if cnt >= max_val:
                    max_val = cnt
                    # print(max_val)
                    _r, _c = r, c
                    # print(r, c)
    return _r, _c


# 제초제 뿌리기
# 제초제는 4개의 대각선 방향으로 퍼짐(벽 혹은 나무 없는 경우 해당 칸 까지만 퍼짐)
# 제초제는 C년만큼 남아있다 C + 1년에 사라짐
# 다시 뿌려지면 C로 갱신
def herbicide(r, c):
    k = K
    global ans
    if grid[r][c] > 0:
        ans += grid[r][c]
        grid[r][c] = 0
        herbi_grid[r][c] = C + 1
        for a, b in ddirs:
            for i in range(1, k + 1):
                nr = r + a * i
                nc = c + b * i
                if border_check(nr, nc):
                    if grid[nr][nc] > 0:
                        ans += grid[nr][nc]
                        grid[nr][nc] = 0
                        herbi_grid[nr][nc] = C + 1
                    elif grid[nr][nc] <= 0:
                        herbi_grid[nr][nc] = C + 1
                        break
    elif grid[r][c] <= 0:
        herbi_grid[r][c] = C + 1


def dilute():
    for r in range(N):
        for c in range(N):
            if herbi_grid[r][c] > 0:
                herbi_grid[r][c] -= 1


# 격자, 진행되는 년 수, 제초제 확산 범위, 제초제 유지 기간
N, M, K, C = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]
herbi_grid = [[0 for _ in range(N)] for _ in range(N)]
dirs = (1, 0), (0, 1), (-1, 0), (0, -1)
ddirs = (1, 1), (1, -1), (-1, 1), (-1, -1)
ans = 0

for i in range(M):
    grid = grow_tree()
    grid = spread()
    r, c = find_coord()
    herbicide(r, c)
    dilute()

print(ans)
