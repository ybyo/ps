class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        c = list(coordinates)
        f, r = c[0], c[1]
        return ord(f) % 2 != int(r) % 2
        