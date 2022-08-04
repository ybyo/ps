class Solution:
    def convertTime(self, current: str, correct: str) -> int:
        ops = [15, 5, 1]
        cu = current.split(':')
        co = correct.split(':')
        cu = list(map(int, cu))
        co = list(map(int, co))
        ans = rem = 0
        if cu[1] <= co[1]:
            ans = co[0] - cu[0]
            rem = co[1] - cu[1]
        else:
            ans = co[0] - cu[0] - 1
            rem = co[1] - cu[1] + 60
        while rem != 0:
            for a in ops:
                ans += rem // a
                rem %= a
        return ans