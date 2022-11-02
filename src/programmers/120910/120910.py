# problem source: https://school.programmers.co.kr/learn/courses/30/lessons/120910

def solution(n, t):
    ans = n
    for _ in range(t):
        ans *= 2
    return ans
