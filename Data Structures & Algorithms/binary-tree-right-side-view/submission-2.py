# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        

#run bfs. at each level in the bfs, take the farthest right value and add it to the result array
    
        result = []
        q = [root] if root else []

        while q:
            farthestRight = None
            lenOfQ = len(q) # must use lenofQ in the for loop because len(q) will be changing

            for _ in range(lenOfQ):
                node = q.pop(0)

                if node:
                    farthestRight = node # need to append left to right,
                                        # so when loop ends, this farthest 
                                        #right is correct
                    if node.left: q.append(node.left)
                    if node.right: q.append(node.right)
            
            result.append(farthestRight.val)
        return result

            



