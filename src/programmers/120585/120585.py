# problem source: https://school.programmers.co.kr/learn/courses/30/lessons/120585

def solution(array, height):
    cnt = 0
    for n in array:
        if n > height:
            cnt += 1

    return cnt
