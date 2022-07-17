class Solution {
public:
    int maximumUniqueSubarray(vector<int> &nums) {
        int n = nums.size();
        int curr_sum = 0;
        int max_sum = 0;
        int ldx = 0;
        int rdx = 0;
        unordered_set<int> set;
        while (rdx < n) {
            while (set.find(nums[rdx]) != set.end()) {
                curr_sum -= nums[ldx];
                set.erase(nums[ldx]);
                ldx++;
            }
            curr_sum += nums[rdx];
            set.insert(nums[rdx]);
            rdx++;
            max_sum = max(max_sum, curr_sum);
        }
        return max_sum;
    }
};
