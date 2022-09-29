import sys

sys.stdin = open("../1204/input.txt", "r")

T = 1
for _ in range(1, T + 1):
    N = int(input())
    ans = []
    for n in range(N):
        tmp = []
        c3 = str(n + 1).count('3')
        c6 = str(n + 1).count('6')
        c9 = str(n + 1).count('9')
        cc = c3 + c6 + c9
        if cc == 1:
            tmp += '-'
        elif cc == 2:
            tmp += '--'
        elif cc == 3:
            tmp += '---'
        else:
            tmp += str(n + 1)
        ans.append(''.join(tmp))
    print(' '.join(ans))
