# problem source: https://school.programmers.co.kr/learn/courses/30/lessons/120825

def solution(my_string, n):
    ans = ""
    for e in my_string:
        for _ in range(n):
            ans += e
    return ans
