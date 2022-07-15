class Solution {
public:
    int dy[4] = {0, -1, 0, 1};
    int dx[4] = {-1, 0, 1, 0};

    static bool check(vector<vector<int>> &grid, int y, int x) {
        return y >= 0 && y < grid.size() && x >= 0 && x < grid[0].size() && grid[y][x] == 1;
    }

    int maxAreaOfIsland(vector<vector<int>> &grid) {
        int m = grid.size(), n = grid[0].size();
        vector<vector<bool>> visited(m, vector<bool>(n, false));
        queue<pair<int, int>> q;
        int ans = 0;
        for (int i = 0; i < m; ++i) {
            for (int j = 0; j < n; ++j) {
                int cnt = 0;
                if (grid[i][j] == 1) {
                    q.emplace(i, j);
                    visited[i][j] = true;
                    while (!q.empty()) {
                        auto [y, x] = q.front();
                        q.pop();
                        cnt++;
                        for (int k = 0; k < 4; ++k) {
                            int ny = y + dy[k];
                            int nx = x + dx[k];
                            if (check(grid, ny, nx) && visited[ny][nx] == false) {
                                q.emplace(ny, nx);
                                visited[ny][nx] = true;
                            }
                        }
                    }
                    ans = max(ans, cnt);
                }
            }
        }
        return ans;
    }
};