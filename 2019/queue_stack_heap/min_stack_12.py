class MinStack:

    def __init__(self):
        # do intialization if necessary
        self.stack = []
        self.minStack = []

    """
    @param: number: An integer
    @return: nothing
    """
    def push(self, number):
        # write your code here
        self.stack.append(number)
        if len(self.minStack) == 0:
            self.minStack.append(number)
        elif number <= self.minStack[-1]:
            self.minStack.append(number)

    """
    @return: An integer
    """
    def pop(self):
        # write your code here
        val = self.stack[-1]
        self.stack.pop(-1)
        if val == self.minStack[-1]:
            self.minStack.pop(-1)
        return val

    """
    @return: An integer
    """
    def min(self):
        # write your code here
        if len(self.minStack) > 0:
            return self.minStack[-1]
        return None

s = MinStack()
s.push(1)
print(s.pop())
s.push(2)
s.push(3)
print(s.min())
s.push(1)
print(s.min())
