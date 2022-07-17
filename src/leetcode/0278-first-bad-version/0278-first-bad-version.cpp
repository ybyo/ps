// The API isBadVersion is defined for you.
// bool isBadVersion(int version);

class Solution {
public:
    int firstBadVersion(int n) {
        int ldx = 0, rdx = n;
        int mid;
        while (ldx <= rdx) {
            mid = ldx + (rdx - ldx) / 2;
            if (isBadVersion(mid)) rdx = mid - 1;
            else ldx = mid + 1;
        }
        return ldx;
    }
};
