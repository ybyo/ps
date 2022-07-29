class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        lt, rt = 0, len(s)
        ans = []
        for x in s:
            if x == 'I':
                ans.append(lt)
                lt += 1
            else:
                ans.append(rt)
                rt -= 1
        return ans + [lt]
        