#include <bits/stdc++.h>

using namespace std;

//leetcode submit region begin(Prohibit modification and deletion)
class Solution {
public:
    int minMoves2(vector<int> &nums) {
        sort(nums.begin(), nums.end());
        int ldx = 0, rdx = nums.size() - 1;
        int ans = 0;
        while (ldx < rdx) {
            ans += abs(nums[rdx--] - nums[ldx++]);
        }
        return ans;
    }
};
//leetcode submit region end(Prohibit modification and deletion)
