# problem source: https://school.programmers.co.kr/learn/courses/30/lessons/12922

def solution(n):
    ans = ((n + 1) // 2) * "수박"
    return ans if n & 1 == 0 else ans[:-1]
