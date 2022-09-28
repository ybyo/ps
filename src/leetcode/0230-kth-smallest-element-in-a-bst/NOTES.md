class Solution:
def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
"""
**Several approaches**
**Follow up**
Topics: Tree, DFS, Binary Search Tree, Binary Tree
"""
stk = []
while True:
while root:
stk.append(root)
root = root.left
root = stk.pop()
k -= 1
if not k:
return root.val
root = root.right # root.right 값을 찾아내면 해당 부분에 대해서 탐색 수행