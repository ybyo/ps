def solution(arr1, arr2):
    ans = [[] for _ in range(len(arr1))]
    for i in range(len(arr1)):
        for j in range(len(arr2[0])):
            ans[i].append(arr1[i][j] + arr2[i][j])
            
    return ans
                