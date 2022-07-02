#include <bits/stdc++.h>

using namespace std;

//leetcode submit region begin(Prohibit modification and deletion)
class Solution {
public:
    bool hasAllCodes(string s, int k) {
        int size = 1 << k;
        int cnt = 0, hash = 0;
        int ones = ~size;
        vector<bool> vec(size, false);
        for (int i = 0; i < s.size(); i++) {
            hash = ((hash << 1) & ones) | (s[i] - '0');
            if (i >= k - 1 && !vec[hash]) {
                vec[hash] = true;
                cnt++;
            }
        }
        return cnt == size;
    }
};
//leetcode submit region end(Prohibit modification and deletion)
