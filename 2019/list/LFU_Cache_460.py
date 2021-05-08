
class Node(object):
    def __init__(self, key, val, times=0):
        self.key = key
        self.val = val
        self.times = times
        self.pre = None
        self.next = None

class LFUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.node_map = {} # <key, Node>
        self.times_map = {} # <times, Node>
        self.capacity = capacity
        self.min_freq = 0

    def add_node_to_tail(self, node):
        if node.times not in self.times_map:
            head = Node(-1, -1)
            tail = Node(-1, -1)
            head.next = tail
            tail.pre = head
            self.times_map[node.times] = [head, tail]
        head, tail = self.times_map[node.times]
        last = tail.pre
        last.next = node
        node.pre = last
        node.next = tail
        tail.pre = node

    def remove_node(self, node):
        pre = node.pre
        next = node.next
        pre.next = next
        next.pre = pre
        head, tail = self.times_map[node.times]
        if head.next == tail and tail.pre == head:
            self.times_map.pop(node.times)

    def delete_least_freq_least_used(self):
        if self.min_freq not in self.times_map: return
        head, tail = self.times_map[self.min_freq]
        first = head.next
        second = first.next
        head.next = second
        second.pre = head
        if second == tail:
            self.times_map.pop(self.min_freq)
        self.node_map.pop(first.key)

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.node_map: return -1
        node = self.node_map[key]
        self.remove_node(node)
        node.times += 1
        self.add_node_to_tail(node)
        if self.min_freq not in self.times_map:
            self.min_freq = node.times
        return node.val

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if self.capacity == 0: return
        if key in self.node_map:
            node = self.node_map[key]
            node.val = value
            self.remove_node(node)
        else:
            node = Node(key, value)
            if len(self.node_map) == self.capacity:
                self.delete_least_freq_least_used()
            self.node_map[key] = node
        node.times += 1
        self.add_node_to_tail(node)
        if self.min_freq not in self.times_map:
            self.min_freq = node.times
        else:
            self.min_freq = min(self.min_freq, node.times)
        print('put', self.min_freq, self.node_map, self.times_map)

# Your LFUCache object will be instantiated and called as such:
obj = LFUCache(0)
obj.put(0, 0)
print(obj.get(0))
'''
obj.put(1, 1)
obj.put(2, 2)
print(obj.get(1))
obj.put(3, 3)
print(obj.get(2))
print(obj.get(3))
obj.put(4, 4)
print(obj.get(1))
print(obj.get(3))
print(obj.get(4))
'''
