#include <bits/stdc++.h>

using namespace std;

//leetcode submit region begin(Prohibit modification and deletion)
class Solution {
public:
    int minCostClimbingStairs(vector<int> &cost) {
        int n = cost.size();
        int ans = 0;
        auto dp = cost;
        for (int i = cost.size() - 3; i >= 0; --i) {
            dp[i] = cost[i] + min(dp[i + 1], dp[i + 2]);
        }
        return min(dp[0], dp[1]);
    }
};
//leetcode submit region end(Prohibit modification and deletion)
