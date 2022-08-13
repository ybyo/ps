class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        tmp = []
        ans = ''
        
        for p in zip(indices, list(s)):
            tmp.append(p)
        tmp.sort()
        for c in tmp:
            ans += c[1]

        return ans