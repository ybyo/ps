class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        else:
            for c in set(s):
                if s.count(c) != t.count(c):
                    return False
                else:
                    pass
        return True