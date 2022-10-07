# problem source: https://school.programmers.co.kr/learn/courses/30/lessons/43165

def solution(numbers, target):
    n = len(numbers)
    global ans
    ans = 0

    def dfs(val, l):
        global ans

        if l == n:
            if val == target:
                ans += 1
            return

        val += numbers[l]
        dfs(val, l + 1)
        val -= numbers[l] * 2
        dfs(val, l + 1)

    dfs(0, 0)

    return ans
