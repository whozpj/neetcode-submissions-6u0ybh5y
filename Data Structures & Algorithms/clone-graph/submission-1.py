"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        

        cloneDict = {}

        def clone(root):
            if not root:
                return None

            if root in cloneDict:
                return cloneDict[root]

            else:

                newNode = Node()
                newNode.val = root.val
                cloneDict[root] = newNode
                
                for neighbor in root.neighbors:
                    newNode.neighbors.append(clone(neighbor))

            
            return newNode

        return clone(node)
            
