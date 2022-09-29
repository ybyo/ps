import sys

sys.stdin = open("../1204/input.txt", "r")


def decode1(c):
    if c.isupper():
        return ord(c) - ord('A')
    if c.islower():
        return ord(c) - ord('a') + 26
    if c.isnumeric():
        return ord(c) - ord('0') + 52
    if c == '+':
        return 62
    if c == '/':
        return 63


def slicer(nums, w):
    return [nums[i:i + w] for i in range(0, len(nums), w)]


T = int(input())
for test_case in range(1, T + 1):
    ans = tmp = ''
    S = list(input())

    for c in S:
        tmp += format(decode1(c), '06b')

    tmp = slicer(tmp, 8)

    for e in tmp:
        ans += chr(int(e, 2))

    print(f"#{test_case}", ans)
