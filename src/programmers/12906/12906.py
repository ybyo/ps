# problem source: https://school.programmers.co.kr/learn/courses/30/lessons/12906

def solution(arr):
    ans = []

    for i in range(len(arr)):
        if not ans:
            ans.append(arr[i])
        else:
            if ans[-1] == arr[i]:
                continue
            else:
                ans.append(arr[i])
    
    return ans
