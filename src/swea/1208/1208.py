import sys

sys.stdin = open("input.txt", "r")

T = 10
for test_case in range(1, T + 1):
    N = int(input())
    S = list(map(int, input().split()))
    ans = 0
    s = sorted(S)
    while N:
        gap = s[-1] - s[0]
        if gap > 1:
            s[-1] -= 1
            s[0] += 1
            s.sort()
        else:
            break
        N = N - 1

    ans = s[-1] - s[0]

    print(f"#{test_case} {ans}")
