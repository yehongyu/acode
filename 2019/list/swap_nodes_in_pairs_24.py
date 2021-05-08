# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head==None or head.next==None: return head
        dummy = ListNode(-1)
        dummy.next = head
        pre = dummy
        cur = head
        while cur and cur.next:
            n1 = cur
            n2 = cur.next
            n3 = n2.next
            pre.next = n2
            n2.next = n1
            n1.next = n3
            cur = n3
            pre = n1
        return dummy.next

s =Solution()
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)

res = s.swapPairs(head)
while res:
    print(res.val)
    res = res.next
