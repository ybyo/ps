#include <bits/stdc++.h>

using namespace std;

//leetcode submit region begin(Prohibit modification and deletion)
class Solution {
#define REP(i, k, n) for (int i = k; i < n; i++)
#define REPR(i, k, n) for (int i = k; i > n; i--)
public:
    vector<int> twoSum(vector<int> &nums, int target) {
        unordered_map<int, int> umap;
        int n = nums.size();
        REP(i, 0, n) {
            if (umap.find(target - nums[i]) != umap.end()) {
                return {i, umap[target - nums[i]]};
            } else umap[nums[i]] = i;
        }
        return {};
    }
};
//leetcode submit region end(Prohibit modification and deletion)
