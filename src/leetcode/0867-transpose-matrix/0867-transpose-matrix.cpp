class Solution {
public:
    vector<vector<int>> transpose(vector<vector<int>> &matrix) {
        vector<int> tmp;
        vector<vector<int>> ans;
        for (int i = 0; i < matrix[0].size(); i++) {
            for (int j = 0; j < matrix.size(); j++) {
                tmp.emplace_back(matrix[j][i]);
            }
            ans.emplace_back(tmp);
            tmp.clear();
        }
        return ans;
    }
};
