class Solution {
public:
    int findKthLargest(vector<int>& nums, int k) {
        priority_queue<int, vector<int>, greater<int>> pq;
        for (int i = 0; i < k; ++i) {
            pq.emplace(nums[i]);
        }
        for (int i = k; i < nums.size(); ++i) {
            if (pq.top() <= nums[i]) {
                pq.pop();
                pq.emplace(nums[i]);
            }
        }
        return pq.top();
    }
};
