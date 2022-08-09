class Solution:
    def wordPattern(self, p: str, s: str) -> bool:
        ss = s.split()
        dct = dict()
        if len(p) != len(ss) or len(set(p)) != len(set(ss)):
            return False
        for i in range(len(ss)):
            if ss[i] not in dct:
                dct[ss[i]] = p[i]
            elif dct[ss[i]] != p[i]:
                return False
        return True