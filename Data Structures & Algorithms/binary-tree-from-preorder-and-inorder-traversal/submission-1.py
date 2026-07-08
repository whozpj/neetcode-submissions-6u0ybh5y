# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        

        if not preorder or not inorder:
            return None

        rootNode = TreeNode(preorder[0])
        mid = inorder.index(preorder[0])

        # Input: preorder = ['1',2,3,4], inorder = [2,'1',3,4]

        #for preOrder, we use 1:mid+1 since mid tells us how many right
        #nodes there are, and we skip the node, then go to the rest (right)
        rootNode.left = self.buildTree(preorder[1:mid+1],inorder[:mid])
        rootNode.right = self.buildTree(preorder[mid+1:],inorder[mid+1:])
        return rootNode

        #keep building left based on pre order
        #when you see something in inorder, stop, go back up one , go right untill you see next inorder