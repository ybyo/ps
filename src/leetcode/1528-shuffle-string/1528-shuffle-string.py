class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        tmp = [''] * len(s)
        
        for i, c in zip(indices, s):
            tmp[i] = c

        return ''.join(tmp)