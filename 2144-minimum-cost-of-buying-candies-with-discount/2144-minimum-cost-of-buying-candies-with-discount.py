class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        ans = cnt = 0
        cost.sort(reverse=True)
        for i in cost:
            cnt += 1
            if cnt % 3 == 0:
                continue
            ans += i
        return ans


class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        cost.sort(reverse=True)
        return sum(cost) - sum(cost[2::3])
