import sys
from collections import Counter

sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    NS = list(map(int, input().split()))

    ans = Counter(NS).most_common()
    print(f"#{test_case} {ans[0][0]}")
