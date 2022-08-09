class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        ans = ''
        while columnNumber:
            curr = (columnNumber-1) % 26
            ans = chr(ord('A')+curr) + ans
            columnNumber = (columnNumber-1) // 26
        return ans