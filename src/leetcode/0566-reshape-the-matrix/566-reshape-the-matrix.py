class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        if r * c != m * n:
            return mat
        ans = [[0] * c for _ in range(r)]
        print(ans)
        for i in range(m * n):
            ans[i // c][i % c] = mat[i // n][i % n]
        return ans