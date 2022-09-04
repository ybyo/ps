class Solution:
    def countAsterisks(self, s: str) -> int:
        ss = s.split('|')
        sss = ''
        for s in ss[::2]:
            sss += s
        return sss.count('*')
            