class Solution:
    def minTimeToType(self, word: str) -> int:
        ans = len(word)
        curr = 'a'
        for c in word:
            # gap = (ord(curr) - ord(c)) % 26
            gap = abs(ord(curr) - ord(c))
            ans += min(gap, 26 - gap)
            curr = c
        return ans