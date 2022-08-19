class Solution:
    def mySqrt(self, x: int) -> int:
        n = (2**31 - 1) // 2
        for nn in range(n - 1):
            if nn * nn == x or nn * nn < x and (nn+1) * (nn+1) > x:
                return nn
                