class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        smap, tmap = Counter(s), Counter(t)
        for c in tmap:
            if c not in smap or tmap[c] == smap[c] + 1:
                return c
        return ''