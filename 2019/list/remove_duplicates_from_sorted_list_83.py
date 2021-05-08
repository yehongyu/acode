# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        cur = head
        while cur != None and cur.next != None:
            if cur.val == cur.next.val:
                tmp = cur.next
                cur.next = cur.next.next
                del tmp
            else:
                cur = cur.next

    def deleteDuplicates_ii(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(-1)
        dummy.next = head
        cur = dummy
        while cur != None and cur.next != None and cur.next.next != None:
            if cur.next.val == cur.next.next.val:
                val = cur.next.val
                node = cur.next.next.next
                while node != None and node.val == val:
                    node = node.next
                cur.next = node
            else:
                cur = cur.next
        return dummy.next


def show_list(head):
    cur = head
    while cur != None:
        print(cur.val, '->', end=' ')
        cur = cur.next
    print('end')

head = ListNode(1)
head.next = ListNode(1)
head.next.next = ListNode(2)
head.next.next.next = ListNode(3)
head.next.next.next.next = ListNode(3)

s = Solution()
show_list(head)
show_list(s.deleteDuplicates_ii(head))
