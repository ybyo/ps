#include <bits/stdc++.h>

using namespace std;

//leetcode submit region begin(Prohibit modification and deletion)
class Solution {
#define REP(i, k, n) for (int i = k; i < n; i++)
#define REPR(i, k, n) for (int i = k; i > n; i--)
public:
    string longestCommonPrefix(vector<string> &strs) {
        int n;
        int min_n = INT_MAX;
        string ans;
        for (auto &str: strs) {
            int n = str.size();
            min_n = min(min_n, n);
        }
        REP(i, 0, min_n) {
            set<char> set;
            for (auto &str: strs) {
                set.emplace(str[i]);
            }
            if (set.size() == 1) {
                ans += strs[0][i];
            } else {
                break;
            }
        }
        return ans;
    }
};
//leetcode submit region end(Prohibit modification and deletion)
