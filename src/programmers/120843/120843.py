# problem source: https://school.programmers.co.kr/learn/courses/30/lessons/120843

def solution(numbers, k):
    ans = 0
    i = 0
    k -= 1

    while k:
        i += 2
        i %= len(numbers)
        k -= 1

    return numbers[i]
