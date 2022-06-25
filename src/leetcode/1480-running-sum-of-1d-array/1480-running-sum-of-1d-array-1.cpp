#include <bits/stdc++.h>

using namespace std;

//leetcode submit region begin(Prohibit modification and deletion)
class Solution {
public:
    vector<int> runningSum(vector<int> &nums) {
        auto ans = nums;
        for (int i = 1; i < ans.size(); i++) {
            ans[i] = ans[i - 1] + nums[i];
        }
        return ans;
    }
};
//leetcode submit region end(Prohibit modification and deletion)
