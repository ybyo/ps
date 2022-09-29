import sys

sys.stdin = open("input.txt", "r")


def recursion(N, K, curr):
    if K == 0:
        return curr

    return recursion(N, K - 1, curr * N)


T = 10
for _ in range(1, T + 1):
    test_case = int(input())
    N, K = map(int, input().split())

    ans = recursion(N, K, 1)

    print(f"#{test_case} {ans}")
