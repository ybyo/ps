# problem source: https://school.programmers.co.kr/learn/courses/30/lessons/120841

def solution(dot):
    a, b = dot[0], dot[1]

    if a > 0 and b > 0:
        return 1
    elif a > 0 and b < 0:
        return 4
    elif a < 0 and b < 0:
        return 3
    elif a < 0 and b > 0:
        return 2
