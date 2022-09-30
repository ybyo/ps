import sys

sys.stdin = open("input.txt", "r")

T = 10
for test_case in range(1, T + 1):
    ans = 0
    _ = int(input())
    S = list(map(int, input().split()))

    for curr in range(2, len(S) - 2):
        k = sorted(S[curr - 2:curr + 3], reverse=True)
        if k[0] == S[curr]:
            ans += k[0] - k[1]

    print(f"#{test_case} {ans}")
