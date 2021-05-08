# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverse(self, head):
        if head == None: return None, None
        if head.next == None: return head, head
        cur = head; pre = None
        while cur:
            next = cur.next
            cur.next = pre
            pre = cur
            cur = next
        return pre, head

    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        dummy = ListNode(-1)
        dummy.next = head
        end = dummy
        while end:
            cur = end
            t = k
            while t > 0 and cur:
                cur = cur.next
                t -= 1
            if t == 0 and cur:
                next = cur.next
                cur.next = None
                cur_h, cur_e = self.reverse(end.next)
                end.next = cur_h
                cur_e.next = next
                end = cur_e
            else:
                end = None
                break
        return dummy.next

s = Solution()
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)
head.next.next.next.next.next = ListNode(6)
head.next.next.next.next.next.next = ListNode(7)
head.next.next.next.next.next.next.next = ListNode(8)
head.next.next.next.next.next.next.next.next = ListNode(9)
#res, end = s.reverse(head)
res = s.reverseKGroup(head, 4)
while res:
    print(res.val)
    res = res.next
