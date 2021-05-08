# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None or head.next==None: return head
        flag = True
        odd_dum = ListNode(-1)
        odd = odd_dum
        even_dum = ListNode(-1)
        even = even_dum
        cur = head
        while cur:
            if flag:
                odd.next = cur
                odd = odd.next
            else:
                even.next = cur
                even = even.next
            flag = not flag
            cur = cur.next
        odd.next = even_dum.next
        even.next = None
        return odd_dum.next

s = Solution()
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)
#head.next.next.next.next.next = ListNode(6)

res = s.oddEvenList(head)
while res:
    print(res.val)
    res = res.next
