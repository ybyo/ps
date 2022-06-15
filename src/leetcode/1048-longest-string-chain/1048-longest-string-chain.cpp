#include <bits/stdc++.h>

using namespace std;

//leetcode submit region begin(Prohibit modification and deletion)
class Solution {
public:
    static bool compare(const string &s1, const string &s2) {
        return s1.size() < s2.size();
    }

    int longestStrChain(vector<string>& words) {
        sort(words.begin(), words.end(), compare);
        unordered_map<string, int> umap;
        int ans = 0;
        for (string &word : words) {
            for (int i = 0; i < word.length(); i++) {
                string pre = word;
                pre.erase(i, 1);
                umap[word] = max(umap[word], umap.find(pre) == umap.end() ? 1 : umap[pre] + 1);
            }
            ans = max(umap[word], ans);
        }
        return ans;
    }
};
//leetcode submit region end(Prohibit modification and deletion)
