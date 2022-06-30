#include <bits/stdc++.h>

using namespace std;

//leetcode submit region begin(Prohibit modification and deletion)
class Solution {
public:
    int minMoves2(vector<int> &nums) {
        sort(nums.begin(), nums.end());
        int mid = nums.size() / 2, ans = 0;
        for (int i = 0; i < nums.size(); ++i) {
            ans += abs(nums[i] - nums[mid]);
        }
        return ans;
    }
};
//leetcode submit region end(Prohibit modification and deletion)
