/*
// Definition for a Node.
class Node {
public:
    int val;
    vector<Node*> children;

    Node() {}

    Node(int _val) {
        val = _val;
    }

    Node(int _val, vector<Node*> _children) {
        val = _val;
        children = _children;
    }
};
*/

class Solution {
public:
    vector<int> preorder(Node *root) {
        vector<int> ans;
        stack<Node *> stk;
        if (root) stk.emplace(root);
        while (!stk.empty()) {
            root = stk.top();
            stk.pop();
            ans.emplace_back(root->val);
            for (auto iter = root->children.rbegin(); iter != root->children.rend(); ++iter) {
                if (*iter) stk.emplace(*iter);
            }
        }
        return ans;
    }
};
