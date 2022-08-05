class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        n, c = len(s), 0
        for d in range(1, len(s)):
            if not len(s) % d:
                seg = s[:d]
                if seg * (len(s) // d) == s:
                    return True
        return False