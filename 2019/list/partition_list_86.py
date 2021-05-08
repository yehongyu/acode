# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        if head == None or head.next == None: return head
        less_dum = ListNode(-1)
        less = less_dum
        more_dum = ListNode(-1)
        more = more_dum
        cur = head
        while cur:
            if cur.val < x:
                less.next = cur
                less = less.next
            else:
                more.next = cur
                more = more.next
            cur = cur.next
        less.next = more_dum.next
        more.next = None
        return less_dum.next
