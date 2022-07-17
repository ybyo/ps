class Solution {
#define REP(i, k, n) for (int i = k; i < n; i++)
#define REPR(i, k, n) for (int i = k; i > n; i--)
public:
    bool check(string s) {
        string rs = s;
        reverse(rs.begin(), rs.end());
        return rs == s;
    }

    int removePalindromeSub(string s) {
        return check(s) ? 1 : 2;
    }
};
