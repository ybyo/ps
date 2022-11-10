# problem source: https://school.programmers.co.kr/learn/courses/30/lessons/120893

def solution(my_string):
    ans = ''
    for i in range(len(my_string)):
        if my_string[i].isupper():
            ans += my_string[i].lower()
        else:
            ans += my_string[i].upper()

    return ans
