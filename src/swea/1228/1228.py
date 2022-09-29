import sys

sys.stdin = open("input.txt", "r")

T = 10
for test_case in range(1, T + 1):
    N = int(input())
    default = list(map(str, input().split()))
    M = int(input())
    command = list(map(str, input().split()))
    i = 0

    while i < len(command):
        m = 0
        if command[i] == 'I':
            idx = int(command[i + 1])
            cnt = int(command[i + 2])
            k = 0
            for j in range(i + 3, i + 3 + cnt):
                default.insert(idx + k, command[j])
                k += 1
                m = j
        i = m + 1

    print(f"#{test_case} {' '.join(default[:10])}")
