class DoubleLinkedNode(object):
    def __init__(self, key, val):
        self.val = val
        self.key = key
        self.pre, self.next = None, None


class LRUCache:
    """
    @param: capacity: An integer
    """
    def __init__(self, capacity):
        self.capacity = capacity
        self.head = DoubleLinkedNode(-1, -1)
        self.tail = DoubleLinkedNode(-1, -1)
        self.head.next = self.tail
        self.tail.pre = self.head
        self.node_map = {}

    """
    @param: key: An integer
    @return: An integer
    """
    def get(self, key):
        val = -1
        if key in self.node_map:
            node = self.node_map[key]
            self.deleteNodeFromList(node)
            self.insertToTail(node)
            val = node.val
        return val

    """
    @param: key: An integer
    @param: value: An integer
    @return: nothing
    """
    def insertToTail(self, node):
        pre = self.tail.pre
        pre.next = node
        node.pre = pre
        node.next = self.tail
        self.tail.pre = node

    def deleteNodeFromList(self, node):
        pre = node.pre
        next = node.next
        pre.next = next
        next.pre = pre
        node.pre = None
        node.next = None

    def set(self, key, value):
        if key in self.node_map:
            node = self.node_map[key]
            self.deleteNodeFromList(node)
            node.val = value
            self.insertToTail(node)
        else:
            if len(self.node_map) == self.capacity:
                self.node_map.pop(self.head.next.key)
                self.deleteNodeFromList(self.head.next)
            node = DoubleLinkedNode(key, value)
            self.insertToTail(node)
            self.node_map[key] = node

s = LRUCache(2)
s.set(2, 1)
s.set(1, 1)
print(s.get(2))
s.set(4, 1)
print(s.get(1))
print(s.get(2))
