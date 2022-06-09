#include <bits/stdc++.h>

using namespace std;

// leetcode submit region begin(Prohibit modification and deletion)
class Solution {
public:
    int countSubstrings(string s) {
        int n = s.size(), cnt = 0;
        vector<vector<int>> grid(n, vector<int>(n));
        for (int k = 0; k < n; k++) {
            for (int i = 0, j = k; j < n; i++, j++) {
                if (k == 0) {
                    cnt++;
                    grid[i][j] = 1;
                } else if (k == 1) {
                    if (s[i] == s[j]) {
                        grid[i][j] = 1;
                        cnt++;
                    } else {
                        grid[i][j] = 0;
                    }
                } else {
                    if (s[i] == s[j] && grid[i + 1][j - 1] == 1) {
                        grid[i][j] = 1;
                        cnt++;
                    } else {
                        grid[i][j] = 0;
                    }
                }
            }
        }
        return cnt;
    }
};
// leetcode submit region end(Prohibit modification and deletion)
