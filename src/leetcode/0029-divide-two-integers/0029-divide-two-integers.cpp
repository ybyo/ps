#include <bits/stdc++.h>

using namespace std;

//leetcode submit region begin(Prohibit modification and deletion)
class Solution {
public:
    int divide(int dividend, int divisor) {
        if (dividend == INT_MIN) {
            if (divisor == -1) return INT_MAX;
            if (divisor < -1) return 1 + divide(dividend - divisor, divisor);
            else return -1 + divide(dividend + divisor, divisor);
        }
        if (divisor == INT_MIN) return 0;
        int abs_dd = abs(dividend);
        int abs_ds = abs(divisor);
        int ans = 0;
        for (int x = 31; x >= 0; x--) {
            if ((abs_dd >> x) >= abs_ds) {
                abs_dd -= (abs_ds << x);
                ans += (1 << x);
            }
        }
        return ((dividend > 0) ^ (divisor > 0)) ? -ans : ans;
    }
};
//leetcode submit region end(Prohibit modification and deletion)
