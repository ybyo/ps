#include <bits/stdc++.h>

using namespace std;

//leetcode submit region begin(Prohibit modification and deletion)
class Solution {
#define REP(i, k, n) for (int i = k; i < n; i++)
#define REPR(i, k, n) for (int i = k; i > n; i--)
public:
    vector<vector<string>> grid;

    bool isValid(vector<string> &board, int r, int c) {
        size_t sz = board.size();
        REP(i, 0, sz) {
            if (board[i][c] == 'Q') return false;
            if (r - i >= 0 && c - i >= 0 && board[r - i][c - i] == 'Q') return false;
            if (r + i < sz && c + i < sz && board[r + i][c + i] == 'Q') return false;
            if (r - i >= 0 && c + i < sz && board[r - i][c + i] == 'Q') return false;
            if (r + i < sz && c - i >= 0 && board[r + i][c - i] == 'Q') return false;
        }
        return true;
    }

    void solve(vector<string> &str, int r) {
        size_t sz = str.size();
        if (r == sz) {
            grid.emplace_back(str);
            return;
        }
        REP(c, 0, sz) {
            if (isValid(str, r, c)) {
                str[r][c] = 'Q';
                solve(str, r + 1);
                str[r][c] = '.';
            }
        }
    }

    vector<vector<string>> solveNQueens(int n) {
        vector<string> board(n, string(n, '.'));
        solve(board, 0);
        return grid;
    }
};
//leetcode submit region end(Prohibit modification and deletion)
