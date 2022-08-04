class Solution:
    def repeatedCharacter(self, s: str) -> str:
        buf = []
        for c in s:
            if c in buf:
                return c
            else:
                buf.append(c)
        return ''