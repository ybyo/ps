class Solution1:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        children = 0
        cookie = 0
        while cookie < len(s) and children < len(g):
            if s[cookie] >= g[children]:
                children += 1
            cookie += 1
        return children


class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        s.sort()
        g.sort()
        pos = ans = 0
        for i in s:
            if pos < len(g):
                if g[pos] <= i:
                    ans += 1
                    pos += 1
            else:
                break
        return ans
