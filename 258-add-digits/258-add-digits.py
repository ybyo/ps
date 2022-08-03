class Solution:
    def addDigits(self, num: int) -> int:
        while num > 9:
            tmp = num
            ttmp = 0
            while tmp:
                ttmp += tmp % 10
                tmp //= 10
            num = ttmp
        return num