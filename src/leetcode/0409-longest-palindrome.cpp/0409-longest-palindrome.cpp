#include <bits/stdc++.h>

using namespace std;

//leetcode submit region begin(Prohibit modification and deletion)
class Solution {
public:
    int longestPalindrome(string s) {
        if (s.size() == 1) return 1;
        if (s.size() == 2 && s[0] == s[1]) return 2;
        int odds = 0;
        for (char c = 'A'; c <= 'z'; ++c) {
            odds += count(s.begin(), s.end(), c) & 1;
        }
        return s.size() - odds + (odds > 0);
    }
};
//leetcode submit region end(Prohibit modification and deletion)
