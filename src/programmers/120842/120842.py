# problem source: https://school.programmers.co.kr/learn/courses/30/lessons/120842

def solution(num_list, n):
    ans = [[] for _ in range(len(num_list) // n)]
    i = 0
    k = 0

    while i < len(num_list):
        ans[k] = num_list[i:i + n]
        i += n
        k += 1

    return ans
