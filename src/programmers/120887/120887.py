# problem source:https://school.programmers.co.kr/learn/courses/30/lessons/120887

from collections import Counter


def solution(i, j, k):
    tmp = ""
    for a in range(i, j + 1):
        tmp += str(a)

    c = Counter(tmp)

    return c[str(k)]
