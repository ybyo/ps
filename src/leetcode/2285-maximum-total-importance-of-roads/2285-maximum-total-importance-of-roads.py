class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        adj_list = {i: [] for i in range(n)}
        ans = 0
        for a, b in roads:
            adj_list[a].append(b)
            adj_list[b].append(a)
        adj_list = dict(sorted(adj_list.items(), key=lambda x: len(x[1]), reverse=True))
        for k, v in adj_list.items():
            ans += n * len(v)
            n -= 1
        return ans