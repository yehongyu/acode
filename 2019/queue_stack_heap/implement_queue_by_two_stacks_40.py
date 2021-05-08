class MyQueue:

    def __init__(self):
        # do intialization if necessary
        self.s1 = []
        self.s2 = []

    """
    @param: element: An integer
    @return: nothing
    """
    def push(self, element):
        # write your code here
        self.s1.append(element)

    """
    @return: An integer
    """
    def pop(self):
        # write your code here
        val = None
        if len(self.s2) == 0 and len(self.s1) > 0:
            for i in range(len(self.s1)):
                self.s2.append(self.s1[-1])
                self.s1.pop(-1)
        if len(self.s2) > 0:
            val = self.s2[-1]
            self.s2.pop(-1)
        return val

    """
    @return: An integer
    """
    def top(self):
        val = None
        if len(self.s2) == 0 and len(self.s1) > 0:
            for i in range(len(self.s1)):
                self.s2.append(self.s1[-1])
                self.s1.pop(-1)
        if len(self.s2) > 0:
            val = self.s2[-1]
        return val

q = MyQueue()
q.push(1)
print(q.pop())
q.push(2)
q.push(3)
print(q.top())
print(q.pop())
