# problem source: https://school.programmers.co.kr/learn/courses/30/lessons/120850

def solution(my_string):
    ans = []
    for i in range(len(my_string)):
        if my_string[i].isdigit():
            ans.append(int(my_string[i]))
    return sorted(ans)
