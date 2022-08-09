class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        p = len(columnTitle) - 1
        ans = 0
        for c in columnTitle:
            ans += (ord(c)-ord('A')+1) * 26**p
            p -= 1
        return ans
            