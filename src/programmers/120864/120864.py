# problem source: https://school.programmers.co.kr/learn/courses/30/lessons/120864

def solution(my_string):
    ans = 0
    tmp = ""
    for c in my_string:
        if c.isdigit():
            tmp += c
        elif tmp != "":
            ans += int(tmp)
            tmp = ""
    if tmp != "":
        ans += int(tmp)
    return ans
