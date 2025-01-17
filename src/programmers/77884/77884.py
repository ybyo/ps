# problem source: https://school.programmers.co.kr/learn/courses/30/lessons/77884

def solution(left, right):
    ans = 0

    for i in range(left, right + 1):
        tmp = 0
        for j in range(1, i + 1):
            if i % j == 0:
                tmp += 1
        if tmp & 1 == 0:
            ans += i
        else:
            ans -= i

    return ans
