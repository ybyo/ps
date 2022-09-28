```
Topics: Tree, DFS, Binary-tree
Pseudo code:
while root dfs:
if root.val == 0:
left and right == 0 or
left and right == null
root.val = null
dfs(root.left)
dfs(root.right)
return root
```
