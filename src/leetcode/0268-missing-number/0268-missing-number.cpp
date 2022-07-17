class Solution {
public:
    int missingNumber(vector<int> &nums) {
        int n = nums.size();
        int sum_nums = 0;
        int sum_i = 0;
        for (int i = 0; i < n; i++) {
            sum_nums += nums[i];
            sum_i += i;
        }
        sum_i += n;
        return sum_i - sum_nums;
    }
};
