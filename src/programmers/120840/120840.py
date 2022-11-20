# problem source: https://school.programmers.co.kr/learn/courses/30/lessons/120840

from math import factorial


def solution(balls, share):
    ans = 0
    return factorial(balls) // (factorial(balls - share) * factorial(share))
