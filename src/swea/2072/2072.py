import sys

sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    ans = 0
    NUMS = list(map(int, input().split()))
    for n in NUMS:
        if n % 2 == 1:
            ans += n

    print(f"#{test_case} {ans}")
