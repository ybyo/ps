class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix[0])
        for r, c in product(range(n // 2 + n % 2), range(n // 2)):
            tmp = matrix[n - 1 - c][r]
            matrix[n - 1 - c][r] = matrix[n - 1 - r][n - c - 1]
            matrix[n - 1 - r][n - c - 1] = matrix[c][n - 1 - r]
            matrix[c][n - 1 - r] = matrix[r][c]
            matrix[r][c] = tmp
            
