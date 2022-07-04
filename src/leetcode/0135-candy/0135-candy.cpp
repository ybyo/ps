#include <bits/stdc++.h>

using namespace std;

//leetcode submit region begin(Prohibit modification and deletion)
class Solution {
public:
    int candy(vector<int> &ratings) {
        int n = ratings.size();
        if (n <= 1) return n;
        int ans = 0;
        vector<int> vec(n, 1);
        for (int i = 1; i < n; ++i) {
            if (ratings[i] > ratings[i - 1]) {
                vec[i] = vec[i - 1] + 1;
            }
        }
        for (int i = n - 1; i > 0; --i) {
            if (ratings[i - 1] > ratings[i]) {
                vec[i - 1] = max(vec[i] + 1, vec[i - 1]);
            }
            ans += vec[i];
        }
        return ans + vec[0];
    }
};
//leetcode submit region end(Prohibit modification and deletion)
