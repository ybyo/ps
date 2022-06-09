#include <bits/stdc++.h>

using namespace std;

//leetcode submit region begin(Prohibit modification and deletion)
class Solution {
public:
    bool checkShareCommon(bitset<26> &a, bitset<26> &b) {
        for (int i = 0; i < 26; i++) {
            if (a[i] && b[i]) return true;
        }
        return false;
    }

    int maxProduct(vector<string> &words) {
        int ans = 0;
        int n = words.size();
        vector<bitset<26>> vec(n);
        for (int i = 0; i < n; i++) {
            for (auto &c: words[i]) {
                vec[i][c - 'a'] = true;
            }
            for (int j = 0; j < i; j++) {
                if (!checkShareCommon(vec[i], vec[j])) {
                    ans = max(ans, (int) (words[i].size() * words[j].size()));
                }
            }
        }
        return ans;
    }
};
//leetcode submit region end(Prohibit modification and deletion)
