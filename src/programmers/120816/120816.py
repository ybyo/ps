# problem source: https://school.programmers.co.kr/learn/courses/30/lessons/120816

def solution(slice, n):
    return n // slice + 1 if n % slice != 0 else n // slice
