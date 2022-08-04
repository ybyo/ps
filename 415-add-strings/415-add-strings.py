class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        nums1, nums2 = list(num1), list(num2)
        ans, carry = [], 0
        while nums1 or nums2:
            n1 = n2 = 0
            if nums1: n1 = ord(nums1.pop()) - ord('0')
            if nums2: n2 = ord(nums2.pop()) - ord('0')
            carry, rem = divmod(n1 + n2 + carry, 10)
            ans.append(rem)
        if carry:
            ans.append(carry)
        return ''.join(str(i) for i in ans)[::-1]