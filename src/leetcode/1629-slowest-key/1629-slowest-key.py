class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        ans_key = ''
        max_latency = 0
        releaseTimes = [0] + releaseTimes
        for i in range(len(releaseTimes)-1):
            key = keysPressed[i]
            latency = releaseTimes[i+1] - releaseTimes[i]
            if latency > max_latency or latency == max_latency and key > ans_key:
                ans_key = key
                max_latency = latency
        return ans_key