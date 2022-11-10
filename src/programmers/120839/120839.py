# problem souce: https://school.programmers.co.kr/learn/courses/30/lessons/120839

def solution(rsp):
    ans = ""
    for i in range(len(rsp)):
        if rsp[i] == "0":
            ans += "5"
        elif rsp[i] == "2":
            ans += "0"
        else:
            ans += "2"

    return ans
