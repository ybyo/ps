# problem source: https://school.programmers.co.kr/learn/courses/30/lessons/120852

def solution(n):
    ans = set()

    while True:
        if n == 1:
            break
        for i in range(2, n + 1):
            if n % i == 0:
                ans.add(i)
                n //= i
                break

    return sorted(list(ans))
