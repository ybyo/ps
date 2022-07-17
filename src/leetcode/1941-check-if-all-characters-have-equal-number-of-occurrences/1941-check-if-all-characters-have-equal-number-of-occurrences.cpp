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
