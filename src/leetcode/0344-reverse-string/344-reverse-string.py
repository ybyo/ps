class Solution:
    def reverseString(self, s: List[str]) -> None:
        lt, rt = 0, len(s) - 1
        tmp = ''
        while lt < rt:
            tmp = s[lt]
            s[lt] = s[rt]
            s[rt] = tmp
            lt += 1
            rt -= 1
        return s
        