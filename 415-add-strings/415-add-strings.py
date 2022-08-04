class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        num1, num2 = list(num1), list(num2)
        carry, ans = 0, []
        while len(num1) or len(num2):
            n1 = ord(num1.pop())-ord('0') if len(num1) else 0
            n2 = ord(num2.pop())-ord('0') if len(num2) else 0
            tmp = n1 + n2 + carry 
            ans.append(tmp % 10)
            carry = tmp // 10
        if carry:
            ans.append(carry)
        return ''.join([str(i) for i in ans])[::-1]