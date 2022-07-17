class Solution {
public:
    int expand(string s, int l, int r) {
        while (l >= 0 && r < s.size() && s[l] == s[r]) {
            l--;
            r++;
        }
        return r - l - 1;
    }

    string longestPalindrome(string s) {
        int l = 0;
        int r = 0;
        int len = 0;
        for (int i = 0; i < s.size(); i++) {
            int odd = expand(s, i, i);
            int even = expand(s, i, i + 1);
            len = max(odd, even);
            if (len > r - l) {
                l = i - (len - 1) / 2;
                r = i + len / 2;
            }
        }
        return s.substr(l, r - l + 1);
    }
};
