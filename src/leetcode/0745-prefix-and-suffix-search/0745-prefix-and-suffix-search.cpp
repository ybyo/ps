class Trie {
    Trie *ch[27];
    int weight;
public:
    Trie() {
        memset(ch, 0, sizeof(ch));
        weight = 0;
    }

    void insert(string str, int wt) {
        Trie *node = this;
        for (char c: str) {
            if (node->ch[c - 'a'] == nullptr) {
                node->ch[c - 'a'] = new Trie();
            }
            node = node->ch[c - 'a'];
            node->weight = wt;
        }
    }

    int prefix(string str) {
        Trie *node = this;
        for (char c: str) {
            if (node->ch[c - 'a'] == nullptr) {
                return -1;
            }
            node = node->ch[c - 'a'];
        }
        return node->weight;
    }
};

class WordFilter {
public:
    Trie root;

    WordFilter(vector<string> &words) {
        int idx = 0;
        for (string word: words) {
            root.insert(word, idx);
            string tmp = '{' + word;
            for (int i = word.length() - 1; i >= 0; i--) {
                string new_word = word[i] + tmp;
                tmp = new_word;
                root.insert(new_word, idx);
            }
            idx++;
        }
    }

    int f(string prefix, string suffix) {
        string word = suffix + '{' + prefix;
        return root.prefix(word);
    }
};

/**
 * Your WordFilter object will be instantiated and called as such:
 * WordFilter* obj = new WordFilter(words);
 * int param_1 = obj->f(prefix,suffix);
 */
