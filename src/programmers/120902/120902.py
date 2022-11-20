# problem source: https://school.programmers.co.kr/learn/courses/30/lessons/120902

def solution(my_string):
    lists = my_string.split()
    print(lists)
    ans = int(lists[0])

    for i in range(1, len(lists) - 1):
        if lists[i] == '+':
            ans += int(lists[i + 1])
        elif lists[i] == '-':
            ans -= int(lists[i + 1])

    return ans
