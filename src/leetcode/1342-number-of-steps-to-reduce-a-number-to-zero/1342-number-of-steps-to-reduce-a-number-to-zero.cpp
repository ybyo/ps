class Solution {
public:
    int numberOfSteps(int num) {
        int cnt = 0;
        if (num == 0) {
            return cnt;
        }
        while (true) {
            if (num == 1) {
                cnt++;
                break;
            }
            if ((num & 1) == 0) {
                cnt++;
            } else {
                cnt = cnt + 2;
            }
            num = num >> 1;
        }
        return cnt;
    }
};
