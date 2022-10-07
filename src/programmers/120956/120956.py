# problem source: https://school.programmers.co.kr/learn/courses/30/lessons/120956

def solution(babbling):
    ans = 0
    able = ['aya', 'ye', 'woo', 'ma']

    for b in babbling:
        if b in able:
            ans += 1
        else:
            tmp = b
            for a in able:
                while a in tmp:
                    idx = tmp.find(a)
                    if tmp[idx:idx + len(a)] == tmp[idx + len(a):idx + len(a) * 2]:
                        break
                    else:
                        tmp = tmp.replace(a, '', 1)
            if len(tmp) == 0:
                ans += 1

    return ans
