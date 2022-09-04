class Solution:
    def countSubstrings(self, s: str) -> int:
        ans = 0

        for i in range(len(s)):
            for lt, rt in (i, i), (i, i + 1):
                while 0 <= lt and rt < len(s) and s[lt] == s[rt]:
                    lt -= 1
                    rt += 1
                    ans += 1

        return ans