#include <bits/stdc++.h>

using namespace std;

//leetcode submit region begin(Prohibit modification and deletion)
class Solution {
#define REP(i, k, n) for (int i = k; i < n; i++)
#define REPR(i, k, n) for (int i = k; i > n; i--)
public:
    vector<int> twoSum(vector<int> &numbers, int target) {
        unordered_map<int, int> umap;
        size_t n = numbers.size();
        REP(i, 0, n) {
            if (umap.find(target - numbers[i]) != umap.end())
                return {umap[target - numbers[i]] + 1, i + 1};
            else
                umap[numbers[i]] = i;
        }
        return {};
    }
};
//leetcode submit region end(Prohibit modification and deletion)
