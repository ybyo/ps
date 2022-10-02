import sys

sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    ans = 0
    arr = [0] * N


    def check(r):
        for c in range(r):
            if arr[r] == arr[c] or abs(arr[r] - arr[c]) == abs(r - c):
                return False
        return True


    def solve(r):
        global ans
        if r == N:
            ans += 1
            return

        for c in range(N):
            arr[r] = c
            if check(r):
                solve(r + 1)


    solve(0)

    print(f"#{test_case} {ans}")
