class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        tot = 0
        money = [0, 0, 0]
        for bill in bills:
            if bill == 5:
                money[0] += 1
            if bill == 10:
                money[1] += 1
                money[0] -= 1
            if bill == 20:
                if money[1] >= 1:
                    money[1] -= 1
                    money[0] -= 1
                else:
                    money[0] -= 3
                money[2] += 1
            for m in money:
                if m <= -1:
                    return False
        return True