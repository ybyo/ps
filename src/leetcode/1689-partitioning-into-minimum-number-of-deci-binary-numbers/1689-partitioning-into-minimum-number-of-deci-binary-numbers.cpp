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
