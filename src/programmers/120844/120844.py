# problem source: https://school.programmers.co.kr/learn/courses/30/lessons/120844

def solution(numbers, direction):
    if len(numbers) == 1:
        return numbers

    if direction == "right":
        numbers.insert(0, numbers[-1])
        numbers.pop()
    else:
        numbers.append(numbers[0])
        numbers.remove(numbers[0])

    return numbers
