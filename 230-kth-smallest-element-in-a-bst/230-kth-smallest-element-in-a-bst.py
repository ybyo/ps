# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        """
        **Several Approaches**
        Topics: Tree, DFS, Binary Search Tree, Binary Tree
        """
        def inorder(r):
            return inorder(r.left) + [r.val] + inorder(r.right) if r else []
                
        return inorder(root)[k - 1]