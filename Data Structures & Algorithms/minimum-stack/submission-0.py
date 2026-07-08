class MinStack:

    def __init__(self):
        self.minStack = []
        self.vals = []

    def push(self, val: int) -> None:
        self.vals.append(val)
        if len(self.minStack) == 0:
            self.minStack.append(val)
        elif self.minStack[-1] < val:
            self.minStack.append(self.minStack[-1])
        else:
            self.minStack.append(val)

    def pop(self) -> None:
        self.minStack.pop()
        return self.vals.pop()

    def top(self) -> int:
        return self.vals[-1]

    def getMin(self) -> int:
        return self.minStack[-1]
        
