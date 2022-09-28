class Solution:
    def numberOfWeakCharacters(self, p: List[List[int]]) -> int:
        ans = max_def_val = 0        
        p.sort(key = lambda x: (-x[0], x[1]))
        
        for _, deff in p:
            if deff < max_def_val:
                ans += 1
            else:
                max_def_val = max(max_def_val, deff)

        return ans
