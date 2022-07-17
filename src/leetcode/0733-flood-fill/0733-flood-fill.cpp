class Solution {
public:
    static bool check(int y, int x, int m, int n) {
        return y >= 0 && y < m && x >= 0 && x < n;
    }

    vector<vector<int>> floodFill(vector<vector<int>> &image, int sr, int sc, int color) {
        int m = image.size(), n = image[0].size();
        int defaultColor = image[sr][sc];
        vector visited(m, vector(n, 0));
        queue<pair<int, int>> q;
        q.emplace(sr, sc);
        array<int, 4> dy = {0, 1, 0, -1};
        array<int, 4> dx = {-1, 0, 1, 0};
        while(!q.empty()) {
            auto [y, x] = q.front();
            image[y][x] = color;
            q.pop();
            for (int i = 0; i < 4; ++i) {
                int ny = y + dy[i];
                int nx = x + dx[i];
                if (check(ny, nx, m, n) && !visited[ny][nx] && image[ny][nx] == defaultColor) {
                    visited[ny][nx] = true;
                    image[ny][nx] = color;
                    q.emplace(ny, nx);
                }
            }

        }
        return image;
    }
};
