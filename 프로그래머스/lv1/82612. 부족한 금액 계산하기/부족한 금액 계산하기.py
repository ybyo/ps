def solution(price, money, count):
    tot = 0
    for i in range(1, count + 1):
        p = price * i
        tot += p

    return tot - money if tot > money else 0
