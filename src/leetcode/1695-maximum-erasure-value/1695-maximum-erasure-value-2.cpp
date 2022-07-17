class Solution {
public:
    int maximumUniqueSubarray(vector<int> &nums) {
        int n = nums.size();
        int curr_sum = 0;
        int max_sum = 0;
        int ldx = 0;
        int rdx = 0;
        array<bool, 100001> arr = {};
        while (rdx < n) {
            curr_sum += nums[rdx];
            if (arr[nums[rdx]]) {
                while (ldx < rdx && nums[ldx] != nums[rdx]) {
                    curr_sum -= nums[ldx];
                    arr[nums[ldx]] = false;
                    ldx++;
                }
                curr_sum -= nums[ldx];
                arr[nums[ldx]] = false;
                ldx++;
            }
            arr[nums[rdx]] = true;
            max_sum = max(max_sum, curr_sum);
            rdx++;
        }
        return max_sum;
    }
};
