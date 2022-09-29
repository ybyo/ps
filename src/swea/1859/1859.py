import sys

sys.stdin = open("../1204/input.txt", "r")
T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    VALS = list(map(int, input().split()))

    ans = 0
    max_val = VALS[-1]

    for val in VALS[N - 3:-1:]:
        if val >= max_val:
            max_val = val
        else:
            ans += max_val - val

    print(f"#{test_case} {ans}")
