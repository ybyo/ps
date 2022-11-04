# problem source: https://school.programmers.co.kr/learn/courses/30/lessons/12910

def solution(arr, divisor):
    ans = [i for i in arr if i % divisor == 0]

    return [-1] if not ans else sorted(ans)
