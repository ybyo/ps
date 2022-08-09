class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        seg = sentence.split()
        for i, s in enumerate(seg):
            if s.find(searchWord) == 0:
                return i + 1
        return -1