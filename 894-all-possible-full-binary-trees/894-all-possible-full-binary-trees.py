# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    memo = {0: [], 1: [TreeNode()]}
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        def deepCopy(node):
            if not node:
                return None
            new_node = TreeNode()
            new_node.left = deepCopy(node.left)
            new_node.right = deepCopy(node.right)
            return new_node
        
        if n % 2 == 0:
            return []
        if n == 1:
            return [TreeNode()]
        
        if n not in Solution.memo:
            ans = []
            for x in range(n):
                y = n - 1 - x
                lb = self.allPossibleFBT(x)
                rb = self.allPossibleFBT(y)
                for lcnt, l in enumerate(lb, 1):
                    for rcnt, r in enumerate(rb, 1):
                        node = TreeNode()
                        node.left = deepCopy(l) if rcnt < len(rb) else l
                        node.right = deepCopy(r) if lcnt < len(lb) else r
                        ans.append(node)
            Solution.memo[n] = ans
        
        
        return Solution.memo[n]
