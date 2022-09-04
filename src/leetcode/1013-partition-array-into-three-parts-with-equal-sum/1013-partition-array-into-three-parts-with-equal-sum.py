class Solution:
    def canThreePartsEqualSum(self, arr: List[int]) -> bool:
        if sum(arr) % 3 != 0:
            return False
        curr = partition = 0
        division = sum(arr) / 3
        for i, n in enumerate(arr):
            curr += n
            if curr == division:
                partition += 1
                curr = 0
        return partition >= 3