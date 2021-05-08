# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        pre = None
        cur = head
        while cur:
            next = cur.next
            cur.next = pre
            pre = cur
            cur = next
        return pre


    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        if head == None or head.next == None: return head
        if m >= n: return head
        k = 0
        dummy = ListNode(-1)
        dummy.next = head
        pre = dummy;
        post = None;
        end = None
        cur = dummy
        while cur:
            k += 1
            if k == m:
                pre = cur
            if k == n+1:
                post = cur.next
                end = cur
            cur = cur.next
        start = pre.next
        pre.next = None
        end.next = None
        self.reverseList(start)
        pre.next = end
        start.next = post
        return dummy.next


s = Solution()
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)

#res = s.reverseList(head)
res = s.reverseBetween(head, 1, 5)
while res:
    print(res.val)
    res = res.next
