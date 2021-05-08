
class Node():
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.pre = None
        self.times = 1

class LRUCache(object):
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.node_map = {}
        self.head = Node(-1, -1)
        self.tail = Node(-1, -1)

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.node_map:
            return None
        node = self.node_map[key]
        self.remove_node_from_list(node)
        self.add_node_to_tail(node)
        return node.value

    def remove_node_from_list(self, node):
        # remove from linked list
        pre = node.pre
        next = node.next
        pre.next = next
        next.pre = pre

    def add_node_to_tail(self, node):
        # add to tail
        last = self.tail.pre
        last.next = node
        node.pre = last
        node.next = self.tail
        self.tail.pre = node

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key in self.node_map:
            node = self.node_map[key]
            self.remove_node_from_list(node)
        node = Node(key, value)
        if len(self.node_map) >= self.capacity:
            first = self.head.next
            self.remove_node_from_list(first)
            self.node_map.pop(first.key)
        self.node_map[key] = node
        self.add_node_to_tail(node)



class LFUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capaciy = capacity
        self.node_map = {} # <key, node>
        self.times_map = {} # <times, doubled linked list>
        self.min_times = None

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.node_map:
            return None
        node = self.node_map[key]
        self.remove_node_from_list(node)
        node.times += 1
        self.add_node_to_list(node)
        return node.value

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key in self.node_map:
            node = self.node_map[key]
            self.remove_node_from_list(node)
        node = Node(key, value)
        if len(self.node_map) >= self.capacity:
            least_node = self.times_map[self.min_times]
            self.remove_node_from_list(least_node)
            self.node_map.pop(least_node.key)
        self.node_map[key] = node
        self.add_node_to_list(node)

    def remove_node_from_list(self, node):
        cur_times = node.times
        pre = node.pre
        next = node.next




class myHashMap(object):
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.lock = None

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """

if __name__ == '__main__':
    # Your LRUCache object will be instantiated and called as such:
    # obj = LRUCache(capacity)
    # param_1 = obj.get(key)
    # obj.put(key,value)
    pass