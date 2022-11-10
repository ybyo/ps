# problem source: https://school.programmers.co.kr/learn/courses/30/lessons/120845

def solution(box, n):
    ans = 1
    for i in range(len(box)):
        ans *= box[i] // n
    return ans
