return:
섬의 갯수
special cond:
모서리의 섬은 제외함
variable:
ans
algorithm:
4방향 탐색
DFS:
더 이상 0을 못찾으면 반환, ans + 1
4방향 0탐색
learned:
* Python 3 빈 배열 만들기:
```python
visited = [[0 for _ in range(c)] for _ in range(r)]
```
* return all([]) 을 활용한 조건 충족
```python
return all([dfs(r - 1, c),
dfs(r + 1, c),
dfs(r, c - 1),
dfs(r, c + 1)])
```
* DFS 진입법
```python
for r, c in product(range(m), range(n)):
if grid[r][c] == 0 and dfs(r, c):
ans += 1
```
참고: https://leetcode.com/problems/number-of-closed-islands/discuss/2210229/Python-Easy-to-understand-DFS-solution-95.50-runtime