class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        a = b = 0
        
        for c in s:
            a += ord(c)
        for c in t:
            b += ord(c)

        return chr(b - a)