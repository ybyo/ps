# problem source: https://school.programmers.co.kr/learn/courses/30/lessons/120830

def solution(n, k):
    service = n // 10
    return 12000 * n + 2000 * (k - service)
