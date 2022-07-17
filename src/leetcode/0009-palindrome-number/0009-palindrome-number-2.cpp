class Solution {
#define REP(i, k, n) for (int i = k; i < n; i++);
#define REPR(i, k, n) for (int i = k; i > n; i--);
public:
    bool isPalindrome(int x) {
        if (0 <= x && x < 10) return true;
        if (x < 0) return false;
        vector<int> vec;
        while (x > 0) {
            int rem = x % 10;
            vec.emplace_back(rem);
            x /= 10;
        }
        int lt = 0;
        int rt = vec.size() - 1;
        while (lt < rt) {
            if (vec[lt] == vec[rt]) {
                lt++;
                rt--;
            } else return false;
        }
        return true;
    }
};
