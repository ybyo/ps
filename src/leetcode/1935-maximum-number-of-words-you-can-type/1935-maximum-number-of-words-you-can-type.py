class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        texts = text.split()
        cnt = 0
        
        for s in texts:
            for c in s:
                if c in brokenLetters:
                    cnt += 1
                    break

        return len(texts) - cnt