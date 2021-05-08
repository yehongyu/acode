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
        arr = []
        dummy = ListNode(-1)
        cur = dummy
        for i in range(len(lists)):
            node = lists[i]
            heapq.heappush(arr, [node.val, i, node])
        while len(arr)>0:
            val, idx, node = heapq.heappop(arr)
            if node.next:
                heapq.heappush(arr, [node.next.val, idx, node.next])
            print(node.val, arr)
            cur.next = node
            cur = node
        cur.next = None
        return dummy.next


s = Solution()
lists = []
l1 = ListNode(1)
l1.next = ListNode(4)
l1.next.next = ListNode(5)
lists.append(l1)

l2 = ListNode(1)
l2.next = ListNode(3)
l2.next.next = ListNode(4)
lists.append(l2)

l3 = ListNode(2)
l3.next = ListNode(6)
lists.append(l3)

head = s.mergeKLists(lists)

while head:
    print(head.val, end='->')
    head = head.next
print('end')



