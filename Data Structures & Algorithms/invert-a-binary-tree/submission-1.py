# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root == None:
            return None

        stack = [ root ]


        while stack:
            current = stack.pop()

            current.right, current.left = current.left, current.right

            if current.right:
                stack.append(current.right)
            if current.left:
                stack.append(current.left)
        return root
