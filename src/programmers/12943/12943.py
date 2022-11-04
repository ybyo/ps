# problem source: https://school.programmers.co.kr/learn/courses/30/lessons/12943

def solution(num):
    if num == 1:
        return 0

    cnt = 0
    while True:
        if num == 1:
            break

        if num & 1 == 1:
            num = num * 3 + 1
        else:
            num //= 2
        cnt += 1

    return -1 if cnt >= 500 else cnt
