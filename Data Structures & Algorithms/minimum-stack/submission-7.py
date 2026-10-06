class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        
        self.stack.append(val)

        if self.minStack:
            # there is already a min on record, so compare with it
            val = min(val, self.minStack[-1])
        # else: minStack is empty, so val is the min and stays as it is

        self.minStack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]
        
