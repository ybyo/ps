#include <bits/stdc++.h>

using namespace std;

//leetcode submit region begin(Prohibit modification and deletion)
class Solution {
public:
    vector<vector<string>>
    suggestedProducts(vector<string> &products, string searchWord) {
        sort(products.begin(), products.end());
        vector<vector<string>> ans;
        int start, bsStart = 0, n = products.size();
        string prefix;
        for (char &c: searchWord) {
            prefix += c;
            start = lower_bound(products.begin() + bsStart, products.end(), prefix) - products.begin();
            ans.emplace_back(initializer_list<string>{});
            for (int i = start; i < min(start + 3, n) && !products[i].compare(0, prefix.length(), prefix); i++) {
                ans.back().emplace_back(products[i]);
            }
            bsStart = start;
        }
        return ans;
    }
};
//leetcode submit region end(Prohibit modification and deletion)
