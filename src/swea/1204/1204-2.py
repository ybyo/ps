import sys

sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    NS = list(map(int, input().split()))

    arr = [0] * 1001
    max_val = -1
    ans = 0

    for i in NS:
        arr[i] += 1
        if arr[i] > max_val:
            max_val = arr[i]
            ans = i
        if arr[i] == max_val:
            ans = max(ans, i)

    print(f"#{test_case} {ans}")
