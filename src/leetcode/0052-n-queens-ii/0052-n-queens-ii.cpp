#include <bits/stdc++.h>

using namespace std;

// leetcode submit region begin(Prohibit modification and deletion)
class Solution {
#define REP(i, k, n) for (int i = k; i < n; i++)
#define REPR(i, k, n) for (int i = k; i > n; i--)
public:
    int solve(vector<bool> &col, vector<bool> &left_diag, vector<bool> &right_diag, int r) {
        int n = col.size();
        int cnt = 0;
        if (r == n) return true;
        REP(i, 0, n) {
            if (!col[i] && !left_diag[r + i] && !right_diag[r - i + n - 1]) {
                col[i] = left_diag[r + i] = right_diag[r - i + n - 1] = true;
                cnt += solve(col, left_diag, right_diag, r + 1);
                col[i] = left_diag[r + i] = right_diag[r - i + n - 1] = false;
            }
        }
        return cnt;
    }

    int totalNQueens(int n) {
        vector<bool> col(n), diag(2 * n - 1), right_diag(2 * n - 1);
        return solve(col, diag, right_diag, false);
    }
};
// leetcode submit region end(Prohibit modification and deletion)
