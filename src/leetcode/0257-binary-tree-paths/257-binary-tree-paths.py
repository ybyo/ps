# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        ans = []
        s = ''
        
        self.dfs(root, s, ans)
        
        return ans

    def dfs(self, node, s, ans):
        s += str(node.val)
        
        if node.left:
            self.dfs(node.left, s + '->', ans)
        if node.right:
            self.dfs(node.right, s + '->', ans)
        if not node.left and not node.right:
            ans.append(s)