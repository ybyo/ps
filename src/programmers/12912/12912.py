# problem source: https://school.programmers.co.kr/learn/courses/30/lessons/12912

def solution(a, b):
    a, b = min(a, b), max(a, b)
    ans = 0
    for i in range(a, b + 1):
        ans += i

    return ans
