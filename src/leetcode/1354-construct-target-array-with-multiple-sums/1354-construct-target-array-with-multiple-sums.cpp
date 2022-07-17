class Solution {
public:
    bool isPossible(vector<int> &target) {
        priority_queue<int> pq(target.begin(), target.end());
        long long sum = 0;
        for (auto &num: target) {
            sum += num;
        }
        while (pq.top() != 1) {
            sum -= pq.top();
            if (sum == 0 || sum >= pq.top()) {
                return false;
            }
            int min_val = pq.top() % sum;
            if (sum != 1 && min_val == 0) {
                return false;
            }
            pq.pop();
            pq.emplace(min_val);
            sum += min_val;
        }
        return true;
    }
};
