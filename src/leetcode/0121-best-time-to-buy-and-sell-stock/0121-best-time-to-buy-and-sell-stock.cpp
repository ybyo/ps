class Solution {
public:
    int maxProfit(vector<int> &prices) {
        int min_val = INT_MAX;
        int ans = INT_MIN;
        for (int i = 0; i < prices.size(); ++i) {
            min_val = min(min_val, prices[i]);
            ans = max(prices[i] - min_val, ans);
        }
        return ans;
    }
};
