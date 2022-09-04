class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        smap = Counter(s)
        tmap = Counter(t)
        for c in tmap:
            if c not in smap or tmap[c] == smap[c] + 1:
                return c
        return ''