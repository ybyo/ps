class Solution:
    def freqAlphabets(self, s: str) -> str:
        """
        Topics: String
        """
        ans = ''
        s = s[::-1]
        i = 0

        while i < len(s):
            if s[i] == '#':
                tmp = s[i + 1 : i + 3]
                tmp = tmp[::-1]
                i += 3
            else:
                tmp = s[i]
                i += 1
            ans += chr(int(tmp) + ord('a') - 1)
        
        return ans[::-1]