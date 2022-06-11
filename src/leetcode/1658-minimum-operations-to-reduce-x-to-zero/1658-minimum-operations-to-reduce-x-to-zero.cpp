#include <bits/stdc++.h>

using namespace std;

//leetcode submit region begin(Prohibit modification and deletion)
class Solution {
#define REP(i, k, n) for (int i = k; i < n; i++)
#define REPR(i, k, n) for (int i = k; i > n; i--)
public:
    int minOperations(vector<int> &nums, int x) {
        int tot_sum = accumulate(nums.begin(), nums.end(), 0);
        if (tot_sum < x) {
            return -1;
        }
        int target = tot_sum - x;
        int n = nums.size();
        int ldx = 0;
        int sum = 0;
        int max_len = -1;
        REP(rdx, 0, n) {
            sum += nums[rdx];
            while (sum > target) {
                sum -= nums[ldx++];
            }
            if (sum == target) {
                max_len = max(max_len, rdx - ldx + 1);
            }
        }
        return max_len == -1 ? -1 : n - max_len;
    }
};
//leetcode submit region end(Prohibit modification and deletion)
