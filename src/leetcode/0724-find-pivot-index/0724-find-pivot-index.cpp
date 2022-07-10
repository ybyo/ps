#include <bits/stdc++.h>

using namespace std;

//leetcode submit region begin(Prohibit modification and deletion)
class Solution {
public:
    int pivotIndex(vector<int> &nums) {
        int lsum = 0, rsum, ans;
        int tot = accumulate(nums.begin(), nums.end(), 0);
        if (tot == nums[0]) return 0;
        for (int i = 1; i < nums.size(); ++i) {
            lsum += nums[i - 1];
            rsum = tot - lsum - nums[i];
            if (lsum == rsum) return i;
        }
        return -1;
    }
};
//leetcode submit region end(Prohibit modification and deletion)
