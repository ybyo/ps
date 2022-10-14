# problem source: https://school.programmers.co.kr/learn/courses/30/lessons/12939

def solution(s):
    ss = list(map(int, s.split()))
    return str(min(ss)) + " " + str(max(ss))
