class Solution:
    def reverseBits(self, n: int) -> int:
        ans = str(bin(n))[::-1][:-2]
        ans += (32-len(ans)) * '0'
        return int(ans, 2)