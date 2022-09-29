import sys

sys.stdin = open("input.txt", "r")

T = 10
for test_case in range(1, T + 1):
    N = input().split()
    M, S = int(N[0]), list(N[1])

    i = 0
    while i < len(S) - 1:
        if S[i] == S[i + 1]:
            del S[i:i + 2]
            i = 0
            continue
        i += 1

    print(f"#{test_case} {''.join(S)}")
