"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        

        hashset = {}
        def clone(node):
            if node in hashset:
                return hashset[node]
            
            if node:
                newNode = Node()
                newNode.val = node.val
                hashset[node] = newNode
                for neighbor in node.neighbors:
                    newNode.neighbors.append(clone(neighbor))

                return newNode
        
        return clone(node)

        
            