#include <bits/stdc++.h>

using namespace std;

//leetcode submit region begin(Prohibit modification and deletion)
class Solution {
public:
    const int MAX_COST = 1e6 + 1;
    int minCost(vector<int> &houses, vector<vector<int>> &cost, int m, int n, int target) {
        vector prevMemo(target + 1, vector(n, MAX_COST));
        for (int color = 1; color <= n; color++) {
            if (houses[0] == color) prevMemo[1][color - 1] = 0;
            else if (!houses[0]) prevMemo[1][color - 1] = cost[0][color - 1];
        }
        for (int house = 1; house < m; house++) {
            vector memo(target + 1, vector(n, MAX_COST));
            for (int neighbor = 1; neighbor <= min(target, house + 1); neighbor++) {
                for (int color = 1; color <= n; color++) {
                    if (houses[house] && color != houses[house]) continue;
                    int currCost = MAX_COST;
                    for (int l = 1; l <= n; l++) {
                        if (l != color) currCost = min(currCost, prevMemo[neighbor - 1][l - 1]);
                        else currCost = min(currCost, prevMemo[neighbor][color - 1]);
                    }
                    int costToPaint = houses[house] ? 0 : cost[house][color - 1];
                    memo[neighbor][color - 1] = currCost + costToPaint;
                }
            }
            prevMemo = memo;
        }
        int minCost = MAX_COST;
        for (int i = 1; i <= n; i++) {
            minCost = min(minCost, prevMemo[target][i - 1]);
        }
        return minCost == MAX_COST ? -1 : minCost;
    }
};
//leetcode submit region end(Prohibit modification and deletion)
