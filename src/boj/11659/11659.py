import sys
from collections import defaultdict

sum_list = [0]
input = sys.stdin.readline

N, M = list(map(int, input().split()))
num_list = list(map(int, input().split()))
curr_sum = 0

for i in range(N):
    curr_sum = curr_sum + num_list[i]
    sum_list.append(curr_sum)

for i in range(M):
    a, b = list(map(int, input().split()))
    range_sum = sum_list[b] - sum_list[a - 1]
    print(range_sum)
