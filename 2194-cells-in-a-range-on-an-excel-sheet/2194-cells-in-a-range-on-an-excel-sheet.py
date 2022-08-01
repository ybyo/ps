class Solution:
    def cellsInRange(self, s: str) -> List[str]:
        c1, c2 = ord(s[0]), ord(s[3])
        r1, r2 = int(s[1]), int(s[4])
        ans = []
        for c in range(c1, c2+1):
            for r in range(r1, r2+1):
                ans.append(chr(c)+str(r))
        return ans