class Solution:
    def numsSameConsecDiff(self, N: int, K: int) -> List[int]:     
        ans = []
        
        def DFS(N, num):
            if not N:
                return ans.append(num)
            tail = num % 10
            next_digits = set([tail + K, tail - K])
            for nd in next_digits:
                if 0 <= nd < 10:
                    nn = num*10 + nd
                    DFS(N - 1, nn)

        for num in range(1, 10):
            DFS(N - 1, num)

        return ans