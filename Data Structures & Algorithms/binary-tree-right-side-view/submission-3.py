# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        #we want to load up all the values onto the queue. once done, we append the rest for the line

        if root == None:
            return []
        
        queue = [ root ]
        result = []

        #bfs
        while queue:
            result.append(queue[-1].val)
            
            tempQ = []
            while queue:
                tempQ.append(queue.pop(0))
            
            for node in tempQ:
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return result

            





