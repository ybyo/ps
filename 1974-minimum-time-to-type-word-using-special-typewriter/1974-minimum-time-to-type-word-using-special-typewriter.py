class Solution:
    def minTimeToType(self, word: str) -> int:
        curr = 'a'
        ans = 0
        for x in word:
            gap = abs(ord(curr) - ord(x))
            if gap <= 13:
                ans += gap
            else:
                ans += (26 - gap)
            curr = x
        return ans + len(word)