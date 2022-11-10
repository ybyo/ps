# problem source: https://school.programmers.co.kr/learn/courses/30/lessons/120823

n = int(input())
ans = ''

for i in range(n):
    for j in range(i + 1):
        ans += '*'
    ans += '\n'

print(ans)
