# problem source: https://school.programmers.co.kr/learn/courses/30/lessons/120892

def solution(cipher, code):
    ans = ''
    for i in range(code - 1, len(cipher), code):
        ans += cipher[i]
    return ans
