#include <bits/stdc++.h>

using namespace std;

//leetcode submit region begin(Prohibit modification and deletion)
class Solution {
public:
    bool checkPossibility(vector<int> &nums) {
        int cnt = 0;
        for (int i = 0; i < nums.size() - 1 && cnt <= 1; ++i) {
            if (nums[i] > nums[i + 1]) {
                cnt++;
                if (i - 1 < 0 || nums[i - 1] <= nums[i + 1]) {
                    nums[i] = nums[i + 1];
                } else {
                    nums[i + 1] = nums[i];
                }
            }
        }
        return cnt <= 1;
    }
};
//leetcode submit region end(Prohibit modification and deletion)
