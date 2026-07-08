"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is None:
            return None

        hashmap = {}
        
        curr = head
        while curr:
            hashmap[curr] = Node(curr.val)
            curr = curr.next
        
        curr = head
        while curr:
            hashmap[curr].next = hashmap.get(curr.next)
            hashmap[curr].random = hashmap.get(curr.random)
            curr = curr.next

        return hashmap[head]


        '''
        hashmap = {}
        def recur(curr):

            if curr is None:
                return None
            if curr in hashmap:
                return hashmap[curr]

            copy = Node(curr.val)
            hashmap[curr] = copy

            copy.next = recur(curr.next)
            copy.random = recur(curr.random)
            return copy

        return recur(head)
        '''
            

            
        