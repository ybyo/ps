# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        st = {}
        ts = {}
        for a, b in zip(s, t):
            if (a not in st) and (b not in ts):
                st[a] = b
                ts[b] = a
            elif st.get(a) != b or ts.get(b) != a:
                return False
        return True
# leetcode submit region end(Prohibit modification and deletion)
