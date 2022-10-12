# problem source: https://school.programmers.co.kr/learn/courses/30/lessons/42862

def solution(n, lost, reserve):
    global ans
    ans = 0
    arr = [1] * n

    for num in lost:
        arr[num - 1] = 0
        if num in reserve:
            arr[num - 1] = 1

    for num in reserve:
        if num in lost:
            continue
        else:
            if num == 1:
                if arr[1] == 0:
                    arr[0] = 1
                    arr[1] = 1
            elif num == n:
                if arr[-2] == 0:
                    arr[-1] = 1
                    arr[-2] = 1
            else:
                if arr[num - 1 + 1] == 0 or arr[num - 1 - 1] == 0:
                    arr[num - 1] = 2

    r = 0
    for i in arr:
        if i == 2:
            r += 1

    tmp = arr[:]

    def recursion(tmp, r, l):
        global ans

        if 0 not in tmp:
            ans = n
            return

        if r == 0 or l >= n:
            cnt = 0
            for i in tmp:
                if i == 0:
                    cnt += 1
            ans = max(ans, n - cnt)
            return

        for i in range(l, len(tmp)):
            if tmp[i] == 2:
                if tmp[i - 1] == 0:
                    tmp[i - 1] = 1
                    tmp[i] = 1
                    recursion(tmp, r - 1, i + 1)
                    tmp[i - 1] = 0
                    tmp[i] = 2
                if tmp[i + 1] == 0:
                    tmp[i + 1] = 1
                    tmp[i] = 1
                    recursion(tmp, r - 1, i + 1)
                    tmp[i - 1] = 0
                    tmp[i] = 2

    recursion(tmp, r, 0)

    return ans
