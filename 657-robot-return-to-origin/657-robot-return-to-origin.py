class Solution:
    def judgeCircle(self, moves: str) -> bool:
        v = h = 0
        for d in moves:
            if d == 'U':
                v += 1
            elif d == 'D':
                v -= 1
            elif d == 'R':
                h += 1
            else:
                h -= 1
        return v == 0 and h == 0
            
        