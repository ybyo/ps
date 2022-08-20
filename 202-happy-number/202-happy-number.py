class Solution:
    def isHappy(self, n: int) -> bool:
        def get_next(n):
            tot = 0
            while n > 0:
                n, d = divmod(n, 10)
                tot += d ** 2
            return tot
    
        seen = set()
    
        while n != 1 and n not in seen:
            seen.add(n)
            n = get_next(n)
    
        return n == 1