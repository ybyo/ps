class Solution:
    def fillCups(self, amount: List[int]) -> int:
        ans = 0
        amount.sort(reverse=True)
        while amount[0] != 0:
            ans += 1
            for i in range(2):
                if amount[i] != 0:
                    amount[i] -= 1
            amount.sort(reverse=True)
        
        return ans