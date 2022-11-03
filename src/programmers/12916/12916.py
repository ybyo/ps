# problem source: https://school.programmers.co.kr/learn/courses/30/lessons/12916

def solution(s):
    ss = s.lower()

    return True if ss.count('p') == ss.count('y') else False
