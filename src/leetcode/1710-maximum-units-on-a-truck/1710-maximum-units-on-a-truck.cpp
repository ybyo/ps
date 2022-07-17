class Solution {
public:
    static bool compare(vector<int> &a, vector<int> &b) {
        return a[1] > b[1];
    }
    int maximumUnits(vector<vector<int>> &boxTypes, int truckSize) {
        int ans = 0;
        sort(boxTypes.begin(), boxTypes.end(), compare);
        for (int i = 0; i < boxTypes.size(); ++i) {
            int box = boxTypes[i][0];
            int unit = boxTypes[i][1];
            while (box > 0 && truckSize > 0) {
                ans += unit;
                box--;
                truckSize--;
            }
        }
        return ans;
    }
};
