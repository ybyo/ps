# problem source: https://school.programmers.co.kr/learn/courses/30/lessons/12903

def solution(s):
    ans = ""
    if len(s) & 1 == 1:
        return s[len(s) // 2]
    else:
        return s[len(s) // 2 - 1: len(s) // 2 + 1]
