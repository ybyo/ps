#include <bits/stdc++.h>

using namespace std;

//leetcode submit region begin(Prohibit modification and deletion)
class Solution {
#define REP(i, k, n) for (int i = k; i < n; i++);
#define REPR(i, k, n) for(int i = k; i > n; i--);
public:
    bool isPalindrome(int x) {
        string str = to_string(x);
        string rstr = str;
        reverse(rstr.begin(), rstr.end());
        if (str == rstr) return true;

        return false;
    }
};
//leetcode submit region end(Prohibit modification and deletion)
