# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def isValid(self, s: str) -> bool:
        d = {'(': ')', '{': '}', '[': ']'}
        stack = []
        for c in s:
            if c in d:
                stack.append(c)
            elif len(stack) == 0 or d[stack.pop()] != c:
                return False
        return len(stack) == 0
# leetcode submit region end(Prohibit modification and deletion)
