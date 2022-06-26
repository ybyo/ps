# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        sdx, tdx = 0, 0
        while sdx < len(s) and tdx < len(t):
            if s[sdx] == t[tdx]:
                sdx += 1
                tdx += 1
            else:
                tdx += 1
        return sdx == len(s)
        
# leetcode submit region end(Prohibit modification and deletion)
