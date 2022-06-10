#include <bits/stdc++.h>

using namespace std;

//leetcode submit region begin(Prohibit modification and deletion)
class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        if (s.empty()) {
            return 0;
        }
        int ldx = 0;
        int rdx = 0;
        int max_len = 1;
        array<int, 256> arr = {};
        while (rdx < s.size()) {
            arr[s[rdx]]++;
            while (arr[s[rdx]] > 1) {
                arr[s[ldx]]--;
                ldx++;
            }
            max_len = max(max_len, rdx - ldx + 1);
            rdx++;
        }
        return max_len;
    }
};
//leetcode submit region end(Prohibit modification and deletion)
