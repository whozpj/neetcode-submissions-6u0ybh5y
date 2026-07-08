# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        result = []

        if root == None:
            return []
        

        queue = [ root ]
        while queue:
            temp = []

            for num in queue:
                temp.append(num.val)
            
            result.append(temp)


            for i in range(0,len(temp)):
                curr = queue.pop(0)

                if curr.left: queue.append(curr.left)
                if curr.right: queue.append(curr.right)

        return result

            
                
            

