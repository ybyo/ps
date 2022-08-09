import heapq

class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        tot = sum(p / t for p, t in classes)
        hp = [(p/t - (p+1)/(t+1), p, t) for p, t in classes]
        heapq.heapify(hp)
        
        for _ in range(extraStudents):
            inc, p, t = heapq.heappop(hp)
            tot -= inc
            p, t = p + 1, t + 1
            heapq.heappush(hp, (p/t - (p+1)/(t+1), p, t))
        
        return tot / len(classes)
