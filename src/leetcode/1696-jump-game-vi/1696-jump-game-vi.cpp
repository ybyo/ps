#include <bits/stdc++.h>

using namespace std;

//leetcode submit region begin(Prohibit modification and deletion)
class Solution {
public:
    int maxResult(vector<int> &nums, int k) {
        int sz = nums.size();
        vector<int> dp(sz);
        deque<int> q = {0};
        dp[0] = nums[0];
        for (int i = 1; i < sz; i++) {
            if (q.front() < i - k) q.pop_front();
            dp[i] = nums[i] + dp[q.front()];
            while (!q.empty() && dp[q.back()] <= dp[i]) {
                q.pop_back();
            }
            q.emplace_back(i);
        }
        return dp.back();
    }
};
//leetcode submit region end(Prohibit modification and deletion)
