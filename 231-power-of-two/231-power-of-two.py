class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
                if n == 0:
                    return False
                if n % 2 == 0:
                    return self.isPowerOfTwo(n // 2)
                
                return n == 2 or n == 1 