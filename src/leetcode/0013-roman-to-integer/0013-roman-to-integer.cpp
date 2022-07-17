class Solution {
#define REP(i, k, n) for (int i = k; i < n; i++)
#define REPR(i, k, n) for (int i = k; i > n; i--)
public:
    int romanToInt(string s) {
        int ans = 0;
        unordered_map<char, int> umap = {
                {'I', 1},
                {'V', 5},
                {'X', 10},
                {'L', 50},
                {'C', 100},
                {'D', 500},
                {'M', 1000}
        };
        REP(i, 0, s.size() - 1) {
            if (umap[s[i]] < umap[s[i + 1]])
                ans -= umap[s[i]];
            else ans += umap[s[i]];
        }
        return ans + umap[s.back()];
    }
};
