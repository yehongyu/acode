# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        import heapq
        heap = []
        dummy = ListNode(-1)
        cur = dummy
        for i in range(len(lists)):
            l = lists[i]
            heapq.heappush(heap, [l.val, i, l])
        while len(heap)>0:
            val, idx, l = heapq.heappop(heap)
            cur.next = l
            cur = cur.next
            l = l.next
            if l:
                heapq.heappush(heap, [l.val, idx, l])
        cur.next = None
        return dummy.next

s = Solution()
l1 = ListNode(1)
l1.next = ListNode(4)
l1.next.next = ListNode(5)
l2 = ListNode(1)
l2.next = ListNode(3)
l2.next.next = ListNode(4)
l3 = ListNode(2)
l3.next = ListNode(6)
res = s.mergeKLists([l1,l2,l3])
while res:
    print(res.val)
    res = res.next

