# problem source: https://school.programmers.co.kr/learn/courses/30/lessons/120896

from collections import Counter


def solution(s):
    ans = ''
    c = Counter(s)

    for k in list(s):
        if c[k] == 1:
            ans += k

    return ''.join(sorted(ans))
