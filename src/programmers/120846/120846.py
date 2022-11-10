# problem source: https://school.programmers.co.kr/learn/courses/30/lessons/120846

def solution(n):
    ans = 0

    def prime(n):
        check = [True] * (n + 1)
        m = int(n ** .5)
        for i in range(2, m + 1):
            if check[i]:
                for j in range(2 * i, n + 1, i):
                    check[j] = False
        return [i for i in range(2, n + 1) if check[i]]

    primes = prime(n)

    for i in range(2, n + 1):
        if i not in primes:
            ans += 1

    return ans
