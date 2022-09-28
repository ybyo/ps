# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]: 
        def dfs(node):
            if not node:
                return False
            lt = dfs(node.left)
            rt = dfs(node.right)
            if not lt:
                node.left = None
            if not rt:
                node.right = None
            return node.val or lt or rt

        return root if dfs(root) else None
        