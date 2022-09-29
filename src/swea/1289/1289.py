import sys

sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    ans = 0
    N = str(input())
    if len(set(N)) == 1:
        if list(set(N))[0] == "0":
            ans = 0
        else:
            ans = 1
    else:
        pre = list(N)[0]
        if pre == "1":
            ans += 1
        for n in list(N[1:]):
            if pre != n:
                ans += 1
                pre = n

    print(f"#{test_case} {ans}")
