class Solution {
public:
    int minDistance(string &word1, string &word2) {
        int n = word1.size();
        int m = word2.size();
        vector grid(n + 1, vector<int> (m + 1));
        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= m; j++) {
                if (word1[i - 1] == word2[j - 1]) {
                    grid[i][j] = grid[i - 1][j - 1] + 1;
                } else {
                    grid[i][j] = max(grid[i - 1][j], grid[i][j - 1]);
                }
            }
        }
        return n + m - 2 * grid[n][m];
    }
};
