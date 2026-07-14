# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        self.best = float('-inf')

        def dp(node):

            if not node:
                return 0
            

            left = max(dp(node.left), 0)
            right = max(dp(node.right), 0)

            self.best = max(self.best, node.val + left + right)

            return node.val + max(left, right)

        
        
        dp(root)
        return self.best

