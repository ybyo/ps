#include <bits/stdc++.h>

using namespace std;

//leetcode submit region begin(Prohibit modification and deletion)
class Solution {
public:
    int furthestBuilding(vector<int> &heights, int bricks, int ladders) {
        priority_queue<int> pq;
        int n = heights.size();
        for (int i = 0; i < n - 1; ++i) {
            int d = heights[i + 1] - heights[i];
            if (d > 0) {
                pq.emplace(-d);
            } else {
                continue;
            }
            if (pq.size() > ladders) {
                bricks += pq.top();
                pq.pop();
                if (bricks < 0) {
                    return i;
                }
            }
        }
        return n - 1;
    }
};
//leetcode submit region end(Prohibit modification and deletion)
