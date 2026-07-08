# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        

        #keep a max along path var while traversing.
        #keep a global result to show.

        self.result = 0
        if root == None:
            return 0

        def dfs(curr, maxAlongPath):

            if curr.val >= maxAlongPath:
                self.result += 1
                maxAlongPath = curr.val

            if curr.right: dfs(curr.right, maxAlongPath)
            if curr.left: dfs(curr.left, maxAlongPath)

        dfs(root, root.val)
        return self.result
            