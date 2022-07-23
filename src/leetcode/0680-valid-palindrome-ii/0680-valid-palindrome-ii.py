class Solution:
    def validPalindrome(self, s: str) -> bool:
        def check(l, r, removed=False):
            while l < r:
                if s[l] != s[r]:
                    if removed:
                        return False
                    return check(l + 1, r, True) or check(l, r - 1, True)
                l += 1
                r -= 1
            return True

        return check(0, len(s) - 1)
