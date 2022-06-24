#include <bits/stdc++.h>

using namespace std;

//leetcode submit region begin(Prohibit modification and deletion)
class TrieNode {
public:
    unordered_map<char, TrieNode *> next;
};

class Solution {
public:
    int minimumLengthEncoding(vector<string> &words) {
        TrieNode *root = new TrieNode;
        vector<pair<TrieNode *, int>> children;
        int ans = 0;
        for (auto &word: set<string>(words.begin(), words.end())) {
            TrieNode *cur = root;
            for (int i = word.size() - 1; i >= 0; --i) {
                if (cur->next.count(word[i]) == 0) {
                    cur->next[word[i]] = new TrieNode;
                }
                cur = cur->next[word[i]];
            }
            children.push_back(make_pair(cur, word.size() + 1));
        }
        for (auto &child: children)
            if ((child.first->next).size() == 0) {
                ans += child.second;
            }
        return ans;
    }
};
//leetcode submit region end(Prohibit modification and deletion)
