class NumMatrix {
    vector<vector<int>> grid;
public:
    NumMatrix(vector<vector<int>> &matrix) {
        int m = matrix.size();
        int n = matrix[0].size();
        if (!m || !n) return;
        grid.resize(m + 1, vector<int>(n + 1));
        for (int r = 1; r <= m; r++) {
            for (int c = 1; c <= n; c++) {
                grid[r][c] += matrix[r - 1][c - 1] + grid[r - 1][c] +
                              grid[r][c - 1] - grid[r - 1][c - 1];
            }
        }
    }

    int sumRegion(int row1, int col1, int row2, int col2) {
        return grid[row2 + 1][col2 + 1] - grid[row1][col2 + 1] -
               grid[row2 + 1][col1] + grid[row1][col1];
    }
};

/**
 * Your NumMatrix object will be instantiated and called as such:
 * NumMatrix* obj = new NumMatrix(matrix);
 * int param_1 = obj->sumRegion(row1,col1,row2,col2);
 */
