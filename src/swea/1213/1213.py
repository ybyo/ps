import sys

sys.stdin = open("input.txt", "rt")

T = 10
for test_case in range(1, T + 1):
    _ = int(input())
    target = str(input())
    S = str(input())

    print(f"#{test_case} {S.count(target)}")
