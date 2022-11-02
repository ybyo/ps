# problem source: https://school.programmers.co.kr/learn/courses/30/lessons/120836

def solution(n):
    ans = 0
    m = int(n ** 0.5)
    for i in range(1, m + 1):
        if n % i == 0:
            ans += 1

    return ans * 2 if m ** 2 != n else (ans - 1) * 2 + 1
