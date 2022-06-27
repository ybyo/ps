#include <bits/stdc++.h>

using namespace std;

//leetcode submit region begin(Prohibit modification and deletion)
class Solution {
public:
    int minPartitions(string n) {
        int max_val = -1;
        for (auto &c : n) {
            max_val = max(c - '0', max_val);
        }
        return max_val;
    }
};
//leetcode submit region end(Prohibit modification and deletion)
