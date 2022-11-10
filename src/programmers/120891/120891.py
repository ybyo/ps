# problem source: https://school.programmers.co.kr/learn/courses/30/lessons/120891

from collections import Counter


def solution(order):
    c = Counter(str(order))
    ans = 0
    if '3' in c:
        ans += c['3']
    if '6' in c:
        ans += c['6']
    if '9' in c:
        ans += c['9']
    return ans
