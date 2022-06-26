#include <bits/stdc++.h>

using namespace std;

//leetcode submit region begin(Prohibit modification and deletion)
class Solution {
public:
    int maxScore(vector<int> &cardPoints, int k) {
        if (cardPoints.size() == k) {
            return accumulate(cardPoints.begin(), cardPoints.end(), 0);
        }
        vector<int> window;
        int sub_sum = 0, ans;
        for (int i = cardPoints.size() - k; i < cardPoints.size(); ++i) {
            window.emplace_back(cardPoints[i]);
        }
        for (int i = 0; i < k; ++i) {
            window.emplace_back(cardPoints[i]);
        }
        for (int i = 0; i < k; ++i) {
            sub_sum += window[i];
        }
        ans = sub_sum;
        for (int i = k; i < window.size(); ++i) {
            sub_sum -= window[i - k];
            sub_sum += window[i];
            ans = max(ans, sub_sum);
        }
        return ans;
    }
};
//leetcode submit region end(Prohibit modification and deletion)
