# problem source: https://school.programmers.co.kr/learn/courses/30/lessons/120831

def solution(n):
    ans = 0
    for i in range(1, n + 1):
        if i & 1 == 0:
            ans += i
    return ans
