# problem source: https://school.programmers.co.kr/learn/courses/30/lessons/120911

def solution(my_string):
    m = my_string.lower()
    return ''.join(sorted(m))
