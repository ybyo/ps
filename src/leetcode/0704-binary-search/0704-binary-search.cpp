class Solution {
public:
    int search(vector<int> &nums, int target) {
        int ldx = 0, rdx = nums.size() - 1;
        int mid;
        while (ldx <= rdx) {
            mid = ldx + (rdx - ldx) / 2;
            if (nums[mid] == target) return mid;
            else if (nums[mid] < target) ldx = mid + 1;
            else rdx = mid - 1;
        }
        return -1;
    }
};
