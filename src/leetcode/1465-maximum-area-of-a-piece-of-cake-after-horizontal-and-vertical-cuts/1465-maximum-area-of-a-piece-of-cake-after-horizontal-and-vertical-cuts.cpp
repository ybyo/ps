class Solution {
public:
    long long m = pow(10, 9) + 7;
    int maxArea(int h, int w, vector<int> &horizontalCuts, vector<int> &verticalCuts) {
        sort(horizontalCuts.begin(), horizontalCuts.end());
        sort(verticalCuts.begin(), verticalCuts.end());
        vector<int> hvec;
        hvec.emplace_back(horizontalCuts[0]);
        for (int i = 1; i < horizontalCuts.size(); i++) {
            hvec.emplace_back(horizontalCuts[i] - horizontalCuts[i - 1]);
        }
        hvec.emplace_back(h - horizontalCuts.back());
        vector<int> wvec;
        wvec.emplace_back(verticalCuts[0]);
        for (int i = 1; i < verticalCuts.size(); i++) {
            wvec.emplace_back(verticalCuts[i] - verticalCuts[i - 1]);
        }
        wvec.emplace_back(w - verticalCuts.back());
        long long a = *max_element(hvec.begin(), hvec.end());
        long long b = *max_element(wvec.begin(), wvec.end());
        return a % m * b % m;
    }
};
