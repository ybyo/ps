#include <bits/stdc++.h>

using namespace std;

//leetcode submit region begin(Prohibit modification and deletion)
struct TrieNode {
    bool end;
    TrieNode *children[26];

    TrieNode() {
        end = false;
        memset(children, NULL, sizeof(children));
    }
};

class Trie {
public:
    Trie() {
        root = new TrieNode();
    }

    ~Trie() {
        clear(root);
    }

    void clear(TrieNode *root) {
        for (int i = 0; i < 26; i++) {
            if (root->children[i]) {
                clear(root->children[i]);
            }
        }
        delete root;
    }

    void insert(string word) {
        TrieNode *dummy = root;
        for (char c: word) {
            if (!dummy->children[c - 'a']) {
                dummy->children[c - 'a'] = new TrieNode();
            }
            dummy = dummy->children[c - 'a'];
        }
        dummy->end = true;
    }

    bool search(string word) {
        TrieNode *dummy = root;
        for (char c: word) {
            if (!dummy->children[c - 'a']) {
                return false;
            }
            dummy = dummy->children[c - 'a'];
        }
        return dummy && dummy->end;
    }

    bool startsWith(string prefix) {
        TrieNode *dummy = root;
        for (char c: prefix) {
            if (!dummy->children[c - 'a']) {
                return false;
            }
            dummy = dummy->children[c - 'a'];
        }
        return dummy;
    }

private:
    TrieNode *root;
};

/**
 * Your Trie object will be instantiated and called as such:
 * Trie* obj = new Trie();
 * obj->insert(word);
 * bool param_2 = obj->search(word);
 * bool param_3 = obj->startsWith(prefix);
 */
//leetcode submit region end(Prohibit modification and deletion)
