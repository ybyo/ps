class Solution {
public:
    int maxScore(vector<int> &cardPoints, int k) {
        int sub_sum = 0, ans;
        int n = cardPoints.size();
        for (int i = 0; i < k; i++) {
            sub_sum += cardPoints[i];
        }
        ans = sub_sum;
        for (int i = 0; i < k; i++) {
            sub_sum += cardPoints[n - i - 1] - cardPoints[k - i - 1];
            ans = max(ans, sub_sum);
        }
        return ans;
    }
};
