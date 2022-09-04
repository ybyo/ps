class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        even = odd = 0
        for p in position:
            if p % 2 == 0:
                even += 1
            else:
                odd += 1
        return min(even, odd)
    