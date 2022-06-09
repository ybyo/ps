#include <bits/stdc++.h>

using namespace std;

//leetcode submit region begin(Prohibit modification and deletion)
class Solution {
public:
    bool areOccurrencesEqual(string s) {
        array<int, 26> arr{};
        int tmp = -1;
        for (auto &c: s) {
            arr[c - 'a']++;
        }
        for (auto &c: arr) {
            if (c != 0) {
                if (tmp == -1) {
                    tmp = c;
                } else {
                    if (c != tmp) {
                        return false;
                    }
                }
            }
        }
        return true;
    }
};
//leetcode submit region end(Prohibit modification and deletion)
