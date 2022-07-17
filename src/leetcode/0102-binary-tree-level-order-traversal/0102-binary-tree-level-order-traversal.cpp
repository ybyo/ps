/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    vector<vector<int>> levelOrder(TreeNode *root) {
        if (root == nullptr) return {};
        vector<vector<int>> ans;
        queue<TreeNode *> q;
        q.emplace(root);
        int sz;
        while (!q.empty()) {
            sz = q.size();
            TreeNode *tmp;
            vector<int> vec;
            for (int i = 0; i < sz; ++i) {
                tmp = q.front();
                q.pop();
                vec.emplace_back(tmp->val);
                if(tmp->left) q.emplace(tmp->left);
                if(tmp->right) q.emplace(tmp->right);
            }
            ans.emplace_back(vec);
        }
        return ans;
    }
};
