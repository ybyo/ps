# problem source: https://school.programmers.co.kr/learn/courses/30/lessons/120848

def solution(n):
    ans = 0
    tot = 1

    while tot <= n:
        ans += 1
        tot *= ans

    return ans - 1
