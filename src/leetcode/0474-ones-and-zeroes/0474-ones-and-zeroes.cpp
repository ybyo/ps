#include <bits/stdc++.h>

using namespace std;

// leetcode submit region begin(Prohibit modification and deletion)
class Solution {
public:
    int findMaxForm(vector<string> &strs, int m, int n) {
        vector<vector<int>> grid(m + 1, vector<int>(n + 1));
        for (auto &str: strs) {
            int zero_cnt = count(str.begin(), str.end(), '0');
            int one_cnt = str.size() - zero_cnt;
            for (int i = m; i >= zero_cnt; i--) {
                for (int j = n; j >= one_cnt; j--) {
                    grid[i][j] = max(grid[i][j], grid[i - zero_cnt][j - one_cnt] + 1);
                }
            }
        }
        return grid[m][n];
    }
};
// leetcode submit region end(Prohibit modification and deletion)
