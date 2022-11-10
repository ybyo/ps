# problem source: https://school.programmers.co.kr/learn/courses/30/lessons/120811

def solution(array):
    array.sort()
    lt, rt, = 0, len(array)
    return array[lt + (rt - lt) // 2]
