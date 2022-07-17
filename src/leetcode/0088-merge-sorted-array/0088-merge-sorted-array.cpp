class Solution {
#define REP(i, k, n) for (int i = k; i < n; i++)
#define REPR(i, k, n) for (int i = k; i > n; i--)
public:
    void merge(vector<int> &nums1, int m, vector<int> &nums2, int n) {
        if (m == 0) nums1 = nums2;
        REPR(i, m + n - 1, 0) {
            if (m == 0 || n == 0) break;
            if (nums1[m - 1] <= nums2[n - 1]) {
                nums1[i] = nums2[n - 1];
                n--;
            } else {
                nums1[i] = nums1[m - 1];
                m--;
            }
        }
        if (m == 0) {
            REP(i, 0, n) {
                nums1[i] = nums2[i];
            }
        }
    }
};
