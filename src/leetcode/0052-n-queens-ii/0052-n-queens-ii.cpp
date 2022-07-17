class Solution {
public:
    int solve(vector<bool> &col, vector<bool> &left_diag, vector<bool> &right_diag, int r) {
        int n = col.size();
        int cnt = 0;
        if (r == n) {
            return 1;
        }
        for (int i = 0; i < n; i++) {
            if (!col[i] && !left_diag[r + i] && !right_diag[r - i + n - 1]) {
                col[i] = left_diag[r + i] = right_diag[r - i + n - 1] = true;
                cnt += solve(col, left_diag, right_diag, r + 1);
                col[i] = left_diag[r + i] = right_diag[r - i + n - 1] = false;
            }
        }
        return cnt;
    }

    int totalNQueens(int n) {
        vector<bool> col(n), left_diag(2 * n - 1), right_diag(2 * n - 1);
        return solve(col, left_diag, right_diag, 0);
    }
};
