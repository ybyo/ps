#include <bits/stdc++.h>

using namespace std;

//leetcode submit region begin(Prohibit modification and deletion)
class Solution {
public:
    int wiggleMaxLength(vector<int> &nums) {
        int up = 1, down = 1;
        for (int i = 1; i < nums.size(); i++)
            if (nums[i] < nums[i - 1]) up = 1 + down;
            else if (nums[i] > nums[i - 1]) down = 1 + up;
        return max(up, down);
    }
};
//leetcode submit region end(Prohibit modification and deletion)
