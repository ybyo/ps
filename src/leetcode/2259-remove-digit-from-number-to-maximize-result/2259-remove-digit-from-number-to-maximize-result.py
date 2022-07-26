class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        ans = 0
        numbers = []
        for i, num in enumerate(list(number)):
            if num == digit:
                numbers.append(number[:i]+number[i+1:])
        numbers.sort()
        return numbers[-1]