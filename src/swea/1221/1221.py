import sys
from collections import Counter

sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    v = list(map(str, input().split()))
    nums = list(map(str, input().split()))
    nums = Counter(nums)
    print(f"{v[0]}")
    for n in ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]:
        for _ in range(nums[n]):
            print(n, end=' ')
    print()
