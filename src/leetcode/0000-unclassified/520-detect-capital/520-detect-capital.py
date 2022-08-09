class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        flag1 = word.isupper()
        flag2 = word[1:].islower()
        flag3 = word.islower()
        
        return flag1 or flag2 or flag3
        