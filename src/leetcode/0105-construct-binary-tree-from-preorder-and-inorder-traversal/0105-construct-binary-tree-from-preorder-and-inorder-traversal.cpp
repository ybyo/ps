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
    int root_idx;
    unordered_map<int, int> umap;
public:
    TreeNode *recursion(vector<int> &preorder, vector<int> &inorder, int left, int right) {
        if (left > right) return nullptr;
        int pivot = umap[preorder[root_idx]];
        TreeNode *node = new TreeNode(inorder[pivot]);
        root_idx++;
        node->left = recursion(preorder, inorder, left, pivot - 1);
        node->right = recursion(preorder, inorder, pivot + 1, right);
        return node;
    }

    TreeNode *buildTree(vector<int> &preorder, vector<int> &inorder) {
        for (int i = 0; i < inorder.size(); ++i) {
            umap[inorder[i]] = i;
        }
        return recursion(preorder, inorder, 0, inorder.size() - 1);
    }
};
