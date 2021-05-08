

def func(n):
    res = 0
    m = 5
    while n >= m:
        res += n // m
        m = m * 5
    return res

class Node():
    def __init__(self, val):
        self.val = val
        self.next = None

def func2(list1, list2):
    if list1 == None or list2 == None: return False
    cur = list1
    while cur.next != None:
        cur = cur.next
    cur.next = list2

    slow = cur.next
    fast = slow
    while fast != None:
        slow = slow.next
        fast = fast.next
        if fast == None: return False
        fast = fast.next
        if fast == slow:
            return True
    return False


list1 = Node(1)
list1.next = Node(2)
list1.next.next = Node(3)
list2 = Node(11)
list2.next = Node(12)
list2.next.next = list1.next

res = func2(list1, list2)
print(res)

