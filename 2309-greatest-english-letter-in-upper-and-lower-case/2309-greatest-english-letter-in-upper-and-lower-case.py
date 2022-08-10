class Solution:
    def greatestLetter(self, s: str) -> str:
        ls = list(s.lower())
        ls.sort(reverse = True)
        
        for c in ls:
            if ls.count(c) >= 2:
                if s.find(c) != -1 and s.find(c.upper()) != -1:
                    return c.upper()
        
        return ''
        