class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        def recursion(k, idx):
            if len(friends) == 1:
                return friends[0]
            idx = (idx + k) % len(friends)
            del friends[idx]
            return recursion(k, idx)

        friends = [i for i in range(n)]
        
        return recursion(k - 1, 0) + 1
