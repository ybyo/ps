#include <bits/stdc++.h>

using namespace std;

//leetcode submit region begin(Prohibit modification and deletion)
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */

class Solution {
public:
    TreeNode *lowestCommonAncestor(TreeNode *root, TreeNode *p, TreeNode *q) {
        int min_val = min(p->val, q->val);
        int max_val = max(p->val, q->val);
        while (root != nullptr) {
            if (root->val > max_val) root = root->left;
            else if (root->val < min_val) root = root->right;
            else return root;
        }
        return nullptr;
    }
};
//leetcode submit region end(Prohibit modification and deletion)
