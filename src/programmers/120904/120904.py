# problem source: https://school.programmers.co.kr/learn/courses/30/lessons/120904

def solution(num, k):
    return list(str(num)).index(str(k)) + 1 if str(k) in list(str(num)) else -1
