# problem source: https://school.programmers.co.kr/learn/courses/30/lessons/120903

def solution(s1, s2):
    cnt = 0
    for c in s1:
        if c in s2:
            cnt += 1
    return cnt
