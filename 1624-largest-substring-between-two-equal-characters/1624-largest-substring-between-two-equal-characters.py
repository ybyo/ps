class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        ov = set()
        ans = 0
        for c in s:
            if s.count(c) >= 2:
                ov.add(c)
        if len(ov) == 0:
            return -1
        print(ov)
        for c in ov:
            tmp = -1
            for i, cc in enumerate(s):
                if c == cc and tmp == -1:
                    tmp = i
                elif c == cc and tmp != -1:
                    ans = max(ans, i - tmp - 1)
        return ans
        