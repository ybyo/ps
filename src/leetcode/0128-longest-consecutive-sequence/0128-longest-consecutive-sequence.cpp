#include <bits/stdc++.h>

using namespace std;

//leetcode submit region begin(Prohibit modification and deletion)
class Solution {
public:
    int longestConsecutive(vector<int> &nums) {
        if (nums.size() == 0) return 0;
        sort(nums.begin(), nums.end());
        int max_val = 0, curr_max = 1;
        for (int i = 1; i < nums.size(); ++i) {
            if (nums[i] == nums[i - 1]) continue;
            else if (nums[i] == nums[i - 1] + 1) curr_max++;
            else {
                max_val = max(max_val, curr_max);
                curr_max = 1;
            }
        }
        return max(max_val, curr_max);
    }
};
//leetcode submit region end(Prohibit modification and deletion)
