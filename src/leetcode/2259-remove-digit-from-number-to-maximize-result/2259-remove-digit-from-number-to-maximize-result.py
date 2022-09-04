class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        idxs = []
        ans = -inf
        for idx, c in enumerate((list(number))):
            if c == digit:
                idxs.append(idx)
        numbers = list(number)
        for idx in idxs:
            tmp = number[:idx] + number[idx + 1:]
            ans = max(ans, int(tmp))
        
        return str(ans)