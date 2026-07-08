#step 1: create a node class. each node looks like this (val, key) since we are
#        storing key value pairs. it is also doubly linked so have prev and next

class Node:
    def __init__(self, val, key):
        self.val = val
        self.key = key
        self.next = None
        self.prev = None


class LRUCache:

# Initialize a hashmap, and also the rightmost and leftmost, which are pointers to
#   the first peice and the last. When we remove the oldest used, we look at left.next
#.  When inserting new, we insert at right.prev
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.hashmap = {}
        self.rightMost = Node(0,0)
        self.leftMost = Node(0,0)

        self.leftMost.next = self.rightMost
        self.rightMost.prev = self.leftMost

#insert helper function: Notes: only deal with inserting at the end, dont worry about
#   dealing with the hashmap stuff here, that is to be dealt with in the main methods
    def insert(self, node):
        temp = self.rightMost.prev
        node.prev = temp
        node.next = self.rightMost
        temp.next = node
        self.rightMost.prev = node
#Similar idea, just focus on removing the node, nothing else
    def remove(self, node):

        nodesPrev = node.prev
        nodesAfter = node.next

        nodesPrev.next = nodesAfter
        nodesAfter.prev = nodesPrev

        node.prev = None
        node.next = None


#function to get the value, need to do a get and then update the order of the linked
    #list
    def get(self, key: int) -> int:
        

        #Edge Case, not there
        if key not in self.hashmap:
            return -1

        #loading up the node that we need to deal with
        nodeToGet = self.hashmap[key]
        #the hashmap stores the nodes, so we dont need to find them in remove or insert

        #remove the node out of the order stack so we can put it in the front
        self.remove(nodeToGet)
        self.insert(nodeToGet)

        #return the found value
        return self.hashmap[key].val


#focus here, kinda aids to get this first try
    def put(self, key: int, value: int) -> None:

        #Case 1: the key we want to add is alr in the map
        if key in self.hashmap:

            #dont create a new node, change its value in place
            node = self.hashmap[key]
            node.val = value

            #standard reorder
            self.remove(node)
            self.insert(node)

        #Case 2: Overflow - we need to remove the first node in list and append 
        #                   this to end
        elif len(self.hashmap) >= self.capacity:

            newNode = Node(value, key)
            del self.hashmap[self.leftMost.next.key]
            self.remove(self.leftMost.next)
            

            self.hashmap[key] = newNode
            self.insert(newNode)
        else:
            newNode = Node(value,key)
            self.hashmap[key] = newNode
            self.insert(newNode)


        
