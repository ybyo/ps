# problem source: https://school.programmers.co.kr/learn/courses/30/lessons/120815

def pizza_counter(a, b):
    res = 1
    min_val = min(a, b)
    max_val = max(a, b)

    while True:
        flag = False
        for k in range(2, min_val + 1):
            if max_val % k == 0 and min_val % k == 0:
                max_val = max_val // k
                min_val = min_val // k
                res *= k
                flag = True
                break
        if flag:
            continue
        else:
            break

    return res * min_val * max_val


def solution(n):
    pizzas = pizza_counter(6, n)
    return pizzas // 6
