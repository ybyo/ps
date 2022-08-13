class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        mp = {c: i for i, c in enumerate(order)}
        
        def check(a, b):
            for adx, bdx in zip(a, b):
                if mp[adx] != mp[bdx]:
                    return mp[adx] < mp[bdx]
            return len(a) <= len(b)
        
        return all(check(a, b) for a, b in zip(words, words[1:]))