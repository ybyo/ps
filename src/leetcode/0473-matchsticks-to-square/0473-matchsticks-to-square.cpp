#include <bits/stdc++.h>

using namespace std;

//leetcode submit region begin(Prohibit modification and deletion)
class Solution {
public:
    static bool recursion(vector<int> &matchsticks, int l, int avg, array<int, 4> &matches) {
        if (l == matchsticks.size()) return count(matches.begin(), matches.end(), avg) == 4;
        for (int i = 0; i < 4; ++i) {
            if (matches[i] + matchsticks[l] > avg) continue;
            int j = i;
            while (--j >= 0) {
                if (matches[i] == matches[j]) break;
            }
            if (j != -1) continue;
            matches[i] += matchsticks[l];
            if (recursion(matchsticks, l + 1, avg, matches)) return true;
            matches[i] -= matchsticks[l];
        }
        return false;
    }

    bool makesquare(vector<int> &matchsticks) {
        int tot = accumulate(matchsticks.begin(), matchsticks.end(), 0);
        if (tot % 4 != 0 || matchsticks.size() < 4) return false;
        int avg = tot / 4;
        array<int, 4> matches{};
        sort(matchsticks.begin(), matchsticks.end(), greater<>());
        return recursion(matchsticks, 0, avg, matches);
    }
};
//leetcode submit region end(Prohibit modification and deletion)
