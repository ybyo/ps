#include <bits/stdc++.h>

using namespace std;

//leetcode submit region begin(Prohibit modification and deletion)
class Solution {
public:
    vector<vector<int>> dir = {{1,  0}, {0,  1}, {-1, 0}, {0,  -1}};
    int mod = 1e9 + 7;
    int grid[51][51][51];
    int recursion(int m, int n, int mxmv, int sr, int sc) {
        if (sr < 0 || sr >= m || sc < 0 || sc >= n && mxmv >= 0) return 1;
        if (mxmv == 0) return 0;
        if (grid[sr][sc][mxmv] != -1) return grid[sr][sc][mxmv];
        int ans = 0;
        for (int i = 0; i < 4; ++i) {
            ans = (ans + recursion(m, n, mxmv - 1, sr + dir[i][0], sc + dir[i][1])) % mod;
        }
        return grid[sr][sc][mxmv] = ans;
    }

    int findPaths(int m, int n, int maxMove, int startRow, int startColumn) {
        memset(grid, -1, sizeof(grid));
        return recursion(m, n, maxMove, startRow, startColumn);
    }
};
//leetcode submit region end(Prohibit modification and deletion)
