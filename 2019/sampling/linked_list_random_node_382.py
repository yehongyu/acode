#coding=utf-8


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
        res = self.head.val
        cur = self.head.next
        count = 1
        while cur != None:
            count += 1
            import numpy as np
            index = np.random.randint(0, count)
            if index == 0:
                res = cur.val
            cur = cur.next
        return res

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
        res = None
        cur = self.head
        cnt = 0
        import random
        while cur:
            p = random.randint(0, cnt)
            if p == 0:
                res = cur.val
            cnt += 1
            cur = cur.next
        return res


# Your Solution object will be instantiated and called as such:
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
obj = Solution(head)
print(obj.getRandom())
