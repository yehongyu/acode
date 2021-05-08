class minStack(object):
    def __init__(self, capacity):
        self.capacity = capacity
        self.stack1 = []
        self.stack2 = []

    def push(self, value):
        if len(self.stack1) >= self.capacity:
            raise Exception("stack is full")
        self.stack1.append(value)
        if len(self.stack2) == 0:
            self.stack2.append(value)
        elif value <= self.stack2[-1]:
            self.stack2.append(value)

    def pop(self):
        if len(self.stack1) == 0:
            raise Exception("stack is empty")
        value = self.stack1.pop(-1)
        if value == self.stack2[-1]:
            self.stack2.pop(-1)
        return value

    def top(self):
        if len(self.stack1) == 0:
            raise Exception("stack is empty")
        value = self.stack1[-1]
        return value

class myQueue():
    def __init__(self, capacity):
        self.capacity = capacity
        self.stack1 = []
        self.stack2 = []

    def push(self, value):
        if len(self.stack1) >= self.capacity:
            raise Exception("queue is full")
        self.stack1.append(value)


    def transfer_data(self):
        while len(self.stack1) > 0:
            self.stack2.append(self.stack1.pop(-1))

    def pop(self):
        value = None
        if len(self.stack2) == 0 and len(self.stack1) > 0:
            self.transfer_data()
        if len(self.stack2) > 0:
            value = self.stack2.pop(-1)
        return value

    def top(self):
        value = None
        if len(self.stack2) == 0 and len(self.stack1) > 0:
            self.transfer_data()
        if len(self.stack2) > 0:
            value = self.stack2[-1]
        return value

