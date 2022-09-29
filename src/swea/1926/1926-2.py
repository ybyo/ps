import sys

sys.stdin = open("../1204/input.txt", "r")

N = int(input())
for n in range(1, N + 1):
    num = list(str(n))
    if '3' in num or '6' in num or '9' in num:
        c3 = num.count('3')
        c6 = num.count('6')
        c9 = num.count('9')
        c = c3 + c6 + c9
        print('-' * c, end=' ')
    else:
        print(n, end=' ')
