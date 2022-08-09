import heapq

class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        tot = sum(p / t for p, t in classes)
        heap = [(p/t - (p+1)/(t+1), p, t) for p, t in classes]
        heapq.heapify(heap)
        
        for _ in range(extraStudents):
            inc, p, t = heapq.heappop(heap)
            tot -= inc
            p, t = p + 1, t + 1
            heapq.heappush(heap, (p/t - (p+1)/(t+1), p, t))
        
        return tot / len(classes)
