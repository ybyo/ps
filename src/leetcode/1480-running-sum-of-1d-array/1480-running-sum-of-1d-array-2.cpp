#include <bits/stdc++.h>

using namespace std;

//leetcode submit region begin(Prohibit modification and deletion)
class Solution {
public:
    vector<int> runningSum(vector<int> &nums) {
        partial_sum(nums.begin(), nums.end(), nums.begin());
        return nums;
    }
};
//leetcode submit region end(Prohibit modification and deletion)
