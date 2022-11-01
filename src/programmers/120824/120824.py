# problem source: https://school.programmers.co.kr/learn/courses/30/lessons/120824

def solution(num_list):
    odd = even = 0
    for e in num_list:
        if e & 1 == 0:
            even += 1
        else:
            odd += 1

    return [even, odd]
