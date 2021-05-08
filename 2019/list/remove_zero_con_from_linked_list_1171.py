# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def removeZeroSumSublists_NN(self, head):
        if head == None: return head
        dummy = ListNode(-1)
        dummy.next = head
        pre = dummy
        l = head
        while l:
            r = l
            cur = 0
            while r:
                cur += r.val
                if cur == 0:
                    pre.next = r.next
                r = r.next
            pre = l
            l = l.next
        return dummy.next

    def removeZeroSumSublists(self, head):
        if head == None: return head
        map = {}
        dummy = ListNode(0)
        dummy.next = head
        cur = head
        sum = 0
        map[0] = dummy
        while cur:
            sum += cur.val
            if sum in map:
                node = map[sum].next
                tmp = sum
                while node != cur and node:
                    tmp += node.val
                    map.pop(tmp)
                    node = node.next
                map[sum].next = cur.next
            else:
                map[sum] = cur
            cur = cur.next
        return dummy.next


s = Solution()
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(-3)
head.next.next.next.next = ListNode(-2)
head.next.next.next.next.next = ListNode(5)

res = s.removeZeroSumSublists(head)
while res:
    print(res.val)
    res = res.next



