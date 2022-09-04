class Solution:
    def maximumSubsequenceCount(self, text: str, pattern: str) -> int:
        ans = cnt0 = cnt1 = 0
        for c in text:
            if c == pattern[1]:
                cnt1 += 1
                ans += cnt0
            if c == pattern[0]:
                cnt0 += 1
        return ans + max(cnt0, cnt1)