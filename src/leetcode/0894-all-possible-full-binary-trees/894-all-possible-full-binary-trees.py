# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    memo = {0: [], 1: [TreeNode()]}

    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        if n not in Solution.memo:
            ans = []
            for x in range(n):
                y = n - 1 - x
                for l in self.allPossibleFBT(x):
                    for r in self.allPossibleFBT(y):
                        node = TreeNode()
                        node.left = l
                        node.right = r
                        ans.append(node)
            Solution.memo[n] = ans

        return Solution.memo[n]
