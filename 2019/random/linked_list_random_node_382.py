# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):

    def __init__(self, head):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        :type head: ListNode
        """
        self.head = head

    def getRandom(self):
        """
        Returns a random node's value.
        :rtype: int
        """
        import random
        cnt = 0
        res = None
        cur = self.head
        while cur != None:
            pro = random.randint(0, cnt)
            if pro == 0: res = cur.val
            cnt += 1
            cur = cur.next
        return res