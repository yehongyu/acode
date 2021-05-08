# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def split(self, head):
        if not head or not head.next: return head, None
        dummy = ListNode(-1)
        slow = dummy
        fast = dummy
        dummy.next = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        l2 = slow.next
        slow.next = None
        return head, l2

    def merge(self, l1, l2):
        dummy = ListNode(-1)
        l3 = dummy
        while l1 or l2:
            if l1 and l2:
                if l1.val < l2.val:
                    l3.next = l1
                    l3 = l3.next
                    l1 = l1.next
                else:
                    l3.next = l2
                    l3 = l3.next
                    l2 = l2.next
            elif l1:
                l3.next = l1
                l3 = l3.next
                l1 = l1.next
            elif l2:
                l3.next = l2
                l3 = l3.next
                l2 = l2.next
        l3.next = None
        return dummy.next


    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next: return head
        l1, l2 = self.split(head)
        print('before:', l1.val, l2.val)
        l1 = self.sortList(l1)
        l2 = self.sortList(l2)
        print('after:', l1.val, l2.val)
        return self.merge(l1, l2)


s = Solution()
head = ListNode(-1)
head.next = ListNode(5)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(0)

res = s.sortList(head)
while res:
    print(res.val)
    res = res.next
