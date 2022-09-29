import sys
from collections import deque

sys.stdin = open("input.txt", "r")

T = 10
for test_case in range(1, T + 1):
    _ = int(input())
    nums = deque(map(int, input().split()))
    ss = [1, 2, 3, 4, 5]
    i = 0
    while True:
        nums[0] -= ss[i]
        nums.append(nums.popleft())
        if nums[-1] <= 0:
            nums[-1] = 0
            break
        i += 1
        i %= 5

    nums = list(map(str, nums))
    ans = ' '.join(nums)

    print(f"#{test_case} {ans}")
