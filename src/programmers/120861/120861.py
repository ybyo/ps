# problem source: https://school.programmers.co.kr/learn/courses/30/lessons/120861

def solution(keyinput, board):
    border_x = board[0] // 2
    border_y = board[1] // 2
    x = y = 0

    def border_check(x, y):
        return -border_x <= x <= border_x and -border_y <= y <= border_y

    for k in keyinput:
        if k == "left":
            if border_check(x - 1, y):
                x -= 1
        if k == "right":
            if border_check(x + 1, y):
                x += 1
        if k == "up":
            if border_check(x, y + 1):
                y += 1
        if k == "down":
            if border_check(x, y - 1):
                y -= 1

    return [x, y]
