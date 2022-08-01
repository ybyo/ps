import string

class Solution:
    def capitalizeTitle(self, title: str) -> str:
        title = string.capwords(title)
        seg = title.split()
        print(seg)
        for i, s in enumerate(seg):
            if len(s) < 3:
                seg[i] = s.lower()
        return " ".join(seg)
                