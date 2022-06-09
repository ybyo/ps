#include <bits/stdc++.h>

using namespace std;

//leetcode submit region begin(Prohibit modification and deletion)
class Solution {
public:
    int longestValidParentheses(string s) {
        if (s.empty()) {
            return 0;
        }
        int ans = 0;
        vector<int> vec(s.size());
        for (int i = 1; i < s.size(); i++) {
            if (s[i] == ')' && i > 0) {
                if (s[i - 1] == '(') {
                    vec[i] = 2 + (i - 2 >= 0 ? vec[i - 2] : 0);
                } else {
                    int idx = i - vec[i - 1] - 1;
                    if (idx >= 0 && s[idx] == '(') {
                        vec[i] = vec[i - 1] + 2 + (idx > 0 ? vec[idx - 1] : 0);
                    }
                }
            }
            ans = max(ans, vec[i]);
        }
        return ans;
    }
};
//leetcode submit region end(Prohibit modification and deletion)
