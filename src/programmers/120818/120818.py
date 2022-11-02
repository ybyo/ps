# problem source: https://school.programmers.co.kr/learn/courses/30/lessons/120818

def solution(price):
    discount = 0

    if 100000 <= price < 300000:
        discount = 5
    elif 300000 <= price < 500000:
        discount = 10
    elif 500000 <= price:
        discount = 20

    return int(price * (100 - discount) / 100)
