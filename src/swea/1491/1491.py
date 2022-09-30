import sys

sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    N, A, B = map(int, input().split())
    k = 0
    mmin = 2147000000

    for n in range(N):
        if n ** 2 > N:
            k = n
            break

    k -= 1

    for r in range(k, 0, -1):
        m = N // r
        for c in range(k, m + 1):
            if r * c <= N:
                curr = A * abs(r - c) + B * (N - r * c)
                if curr < mmin:
                    mmin = curr

    print(f"#{test_case} {mmin}")
