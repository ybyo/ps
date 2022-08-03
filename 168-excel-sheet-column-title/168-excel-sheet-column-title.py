class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        ans = ''
        while columnNumber > 0:
            tmp = columnNumber % 26 + ord('A') - 1
            if tmp < ord('A'):
                tmp += 26
                columnNumber -= 1
            ans = chr(tmp) + ans
            columnNumber //= 26
        return ans
            