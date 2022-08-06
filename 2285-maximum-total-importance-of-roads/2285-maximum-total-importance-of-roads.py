import heapq
class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        ans = 0
        values = [0] * n
        for a, b in roads:
            values[a] += 1
            values[b] += 1
        heapq.heapify(values)
        w = 1
        while values:
            ans += heapq.heappop(values) * w
            w += 1
        return ans