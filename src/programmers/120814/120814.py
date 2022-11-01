# problem source: https://school.programmers.co.kr/learn/courses/30/lessons/120814

def solution(n):
    return n // 7 + 1 if n % 7 != 0 else n // 7
