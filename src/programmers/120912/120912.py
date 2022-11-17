# problem source: https://school.programmers.co.kr/learn/courses/30/lessons/120912

from collections import Counter


def solution(array):
    s = list(''.join(map(str, array)))
    c = Counter(s)

    return c['7']
