class Solution:
    def firstUniqChar(self, s: str) -> int:
        abc = "abcdefghijklmnopqrstuvwxyz"
        ans = 10**5
        for c in abc:
            idx = s.find(c);
            if (idx != -1 and idx == s.rfind(c)):
                ans = min(ans, idx)
        return ans if ans < 10**5 else -1