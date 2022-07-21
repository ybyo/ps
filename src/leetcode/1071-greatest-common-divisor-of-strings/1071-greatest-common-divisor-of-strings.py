class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1 + str2 != str2 + str1:
            return ''
        limit = gcd(len(str1), len(str2))
        while limit:
            str11 = str1[:limit]
            str22 = str2[:limit]
            if str11 == str22:
                return str1[:limit]
            limit -= 1
        return ''


class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1 + str2 != str2 + str1:
            return ''
        if str1 == str2:
            return str1
        if len(str1) > len(str2):
            str1 = str1[len(str2):]
            return self.gcdOfStrings(str1, str2)
        if len(str2) > len(str1):
            str2 = str2[len(str1):]
            return self.gcdOfStrings(str1, str2)


class Solution:
    def gcdOfStrings(self, s1: str, s2: str) -> str:
        return s1[:gcd(len(s1), len(s2))] if s1 + s2 == s2 + s1 else ''


class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        def gcd(a: int, b: int) -> int:
            return b if a == 0 else gcd(b % a, a)

        d = gcd(len(str1), len(str2))
        return str1[: d] if str1[: d] * (len(str2) // d) == str2 and str2[: d] * (len(str1) // d) == str1 else ''


class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        def gcd(a: int, b: int) -> int:
            return b if a == 0 else gcd(b % a, a)

        d = gcd(len(str2), len(str2))
        gcd_str = str2[0: d]
        ptn = '(' + gcd_str + ')+'
        return gcd_str if re.fullmatch(ptn, str2) and re.fullmatch(ptn, str2) else ''
