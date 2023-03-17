import sys

# sys.stdin = open("input.txt", "r")

_ = input()
num = list(input())
ans = 0

for n in num:
    ans = ans + int(n)

print(ans)
