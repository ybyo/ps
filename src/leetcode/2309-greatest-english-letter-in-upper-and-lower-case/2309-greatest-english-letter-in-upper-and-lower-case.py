class Solution:
    def greatestLetter(self, s: str) -> str:
        ss = set(s)
        for c in 'ZYXWVUTSRQPONMLKJIHGFEDCBA':
            if c.lower() in ss and c in ss:
                return c
        return ''