# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def check(self, s: str) -> str:
        imap = {}
        new_str = []
        for i, c in enumerate(s):
            if c not in imap:
                imap[c] = i
            new_str.append(str(imap[c]))
            print(new_str)
        return ' '.join(new_str)

    def isIsomorphic(self, s: str, t: str) -> bool:
        return self.check(s) == self.check(t)
# leetcode submit region end(Prohibit modification and deletion)
