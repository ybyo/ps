class Solution:
    def decodeString(self, s: str) -> str:
        dq = deque()
        val = 0
        ans = ''

        for c in s:
            if c == '[':
                dq.append(ans)
                dq.append(val)
                val = 0
                ans = ''
            elif c == ']':
                num = dq.pop()
                prev = dq.pop()
                ans = prev + num*ans
            elif c.isdigit():
                val = val*10 + int(c)
            else:
                ans += c

        return ans
                