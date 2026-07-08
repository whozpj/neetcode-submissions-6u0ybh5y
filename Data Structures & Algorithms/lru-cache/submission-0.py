class Node:
    def __init__(self, val, key):
        self.val = val
        self.key = key
        self.next = None
        self.prev = None


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.hashmap = {}
        self.rightMost = Node(0,0)
        self.leftMost = Node(0,0)

        self.leftMost.next = self.rightMost
        self.rightMost.prev = self.leftMost

    def insert(self, node):
        temp = self.rightMost.prev
        node.prev = temp
        node.next = self.rightMost
        temp.next = node
        self.rightMost.prev = node

    def remove(self, node):

        nodesPrev = node.prev
        nodesAfter = node.next

        nodesPrev.next = nodesAfter
        nodesAfter.prev = nodesPrev

        node.prev = None
        node.next = None



    def get(self, key: int) -> int:

        if key not in self.hashmap:
            return -1

        nodeToGet = self.hashmap[key]
        #the hashmap stores the nodes, so we dont need to find them in remove or insert

        self.remove(nodeToGet)
        self.insert(nodeToGet)

        return self.hashmap[key].val

    def put(self, key: int, value: int) -> None:
        
        if key in self.hashmap:
            node = self.hashmap[key]

            node.val = value

            self.remove(node)
            self.insert(node)
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


        
