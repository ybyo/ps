class Solution:
    def balancedStringSplit(self, s: str) -> int:
        balance = ans = 0
        for x in s:
            if x == 'R':
                balance += 1
            else:
                balance -= 1
            if balance == 0:
                ans += 1
        return ans