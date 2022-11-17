# problem source: https://school.programmers.co.kr/learn/courses/30/lessons/120890

def solution(array, n):
    tmp = []
    array.sort()
    for num in array:
        tmp.append(abs(n - num))

    return array[tmp.index(min(tmp))]
