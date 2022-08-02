class Solution:
    def firstUniqChar(self, s: str) -> int:
        cnt = collections.Counter(s)
        for i, c in enumerate(s):
            if cnt[c] == 1:
                return i
        return -1