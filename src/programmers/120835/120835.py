# problem source: https://school.programmers.co.kr/learn/courses/30/lessons/120835

def solution(emergency):
    tmp = emergency[:]
    tmp.sort(reverse=True)
    ans = []
    for i in range(len(emergency)):
        ans.append(tmp.index(emergency[i]) + 1)
    return ans
