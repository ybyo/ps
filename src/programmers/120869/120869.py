# problem source: https://school.programmers.co.kr/learn/courses/30/lessons/120869

def solution(spell, dic):
    s = ''.join(sorted(spell))
    tmp = []

    for d in dic:
        if len(d) == len(s):
            dd = sorted(d)
            if s == ''.join(dd):
                return 1

    return 2
