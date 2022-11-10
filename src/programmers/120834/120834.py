# problem source: https://school.programmers.co.kr/learn/courses/30/lessons/120834

def solution(age):
    tmp = list(str(age))
    for i in range(len(tmp)):
        tmp[i] = chr(int(tmp[i]) + ord('a'))

    return ''.join(tmp)
