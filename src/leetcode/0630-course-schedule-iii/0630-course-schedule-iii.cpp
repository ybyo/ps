#include <bits/stdc++.h>

using namespace std;

//leetcode submit region begin(Prohibit modification and deletion)
class Solution {
public:
    int scheduleCourse(vector<vector<int>> &courses) {
        sort(courses.begin(), courses.end(),
             [](auto &a, auto &b) { return a[1] < b[1]; });
        priority_queue<int> pq;
        int duration_sum = 0;
        for (auto course: courses) {
            duration_sum += course[0];
            pq.emplace(course[0]);
            if (duration_sum > course[1]) {
                duration_sum -= pq.top();
                pq.pop();
            }
        }
        return pq.size();
    }
};
//leetcode submit region end(Prohibit modification and deletion)
