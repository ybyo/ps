#include <bits/stdc++.h>

using namespace std;

//leetcode submit region begin(Prohibit modification and deletion)
class Solution {
public:
    int minDeletions(string s) {
        vector<int> vec(26, 0);
        for (int i = 0; i < s.size(); ++i) {
            vec[s[i] - 'a']++;
        }
        sort(vec.begin(), vec.end());
        int ans = 0, max_val;
        for (int i = 24; i >= 0; --i) {
            if (vec[i] == 0) {
                break;
            }
            if (vec[i] >= vec[i + 1]) {
                max_val = vec[i];
                vec[i] = vec[i + 1] - 1;
                if (vec[i] < 0) {
                    vec[i] = 0;
                }
                ans += max_val - vec[i];
            }
        }
        return ans;
    }
};
//leetcode submit region end(Prohibit modification and deletion)
