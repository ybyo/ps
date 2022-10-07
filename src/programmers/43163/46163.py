# problem source: https://school.programmers.co.kr/learn/courses/30/lessons/43163

from collections import deque
import string

alphabet = list(string.ascii_lowercase)


def solution(begin, target, words):
    if target not in words:
        return 0

    dq = deque()
    visited = {}

    for i in range(len(words)):
        visited[words[i]] = 0

    for i in range(len(begin)):
        dq.append((begin[:i] + begin[i + 1:], i, 0))

    ans = 51

    while dq:
        s, idx, cnt = dq.popleft()
        for a in alphabet:
            ns = s[:idx] + a + s[idx:]
            if ns == target:
                ans = min(ans, cnt + 1)
            elif ns in words:
                if visited[ns] == 0:
                    visited[ns] = 1
                    for j in range(len(begin)):
                        dq.append((ns[:j] + ns[j + 1:], j, cnt + 1))

    return ans
