class Solution {
public:
    bool hasAllCodes(string s, int k) {
        if (s.size() < k) return false;
        set<string> set;
        for (int i = 0; i <= s.size() - k; i++) {
            set.insert(s.substr(i, k));
        }
        return set.size() == (1 << k);
    }
};
