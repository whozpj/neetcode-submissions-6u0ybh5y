# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:

        memo = {}
        def search(node):

            if not node:
                return 0
            
            if node in memo:
                return memo[node]

            leftDontTake = search(node.left)
            rightDontTake = search(node.right)


            left = 0
            right = 0
            if node.right:
                right = search(node.right.left) + search(node.right.right)
            if node.left:
                left = search(node.left.left) + search(node.left.right)


            memo[node] =  max(leftDontTake + rightDontTake, node.val + left + right)
            return memo[node]

        return search(root)