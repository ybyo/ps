#include <bits/stdc++.h>

using namespace std;

//leetcode submit region begin(Prohibit modification and deletion)
class Solution {
public:
    int findKthLargest(vector<int> &nums, int k) {
        sort(nums.rbegin(), nums.rend());
        set<int> set;
        int sz = set.size();
        int idx = 0, tmp;
        for (auto &n: nums) {
            if (n == tmp) {
                k--;
            }
            set.emplace(n);
            idx++;
            if (set.size() == k) {
                return n;
            }
            tmp = n;
        }
        return -1;
    }
};
//leetcode submit region end(Prohibit modification and deletion)
