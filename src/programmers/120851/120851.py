# problem source: https://school.programmers.co.kr/learn/courses/30/lessons/120851

def solution(my_string):
    ans = 0
    for i in range(len(my_string)):
        if my_string[i].isdigit() and int(my_string[i]) > 0:
            ans += int(my_string[i])
    return ans
