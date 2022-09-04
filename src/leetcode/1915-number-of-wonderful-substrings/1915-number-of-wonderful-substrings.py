class Solution:
    def wonderfulSubstrings(self, word: str) -> int:
        cnt = [0] * 1024
        cnt[0] = 1
        ans = curr = 0

        for c in word:
            curr ^= 1 << (ord(c) - ord('a'))
            ans += cnt[curr]

            for i in range(10):
                new_bitmask = curr ^ (1 << i)
                if cnt[new_bitmask] > 0:
                    ans += cnt[new_bitmask]
            cnt[curr] += 1

        return ans
