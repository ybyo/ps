# problem source: https://school.programmers.co.kr/learn/courses/30/lessons/120888

def solution(my_string):
    s = list(my_string)
    ans = []
    for i in range(len(s)):
        if s[i] in ans:
            continue
        else:
            ans.append(s[i])

    return ''.join(ans)
