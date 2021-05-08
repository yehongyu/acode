# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
class Node(object):
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child

class Solution(object):
    def numComponents(self, head, G):
        """
        :type head: ListNode
        :type G: List[int]
        :rtype: int
        """
        nodes = set()
        for num in G:
            nodes.add(num)
        cur = head
        cnt = 1
        while cur:
            if cur.val in nodes and (cur.next == None or cur.next.val not in nodes):
                cnt += 1
        return cnt

    def get_list_size(self, root):
        size = 0
        cur = root
        while cur:
            cur = cur.next
            size += 1
        return size

    def splitListToParts(self, root, k):
        size = self.get_list_size(root)
        split_size = size // k + 1
        greater = size % k
        res = []
        cur = root
        for i in range(k):
            res.append(cur)
            if i >= greater: split_size -= 1
            cnt = split_size
            pre = None
            while cur and cnt > 0:
                pre = cur
                cur = cur.next
                cnt -= 1
            if not pre: pre.next = None
        return res

    def flatten_helper(self, head):
        if head == None: return head, head
        cur = head
        next = cur.next
        if cur.child:
            cur_h, cur_e = self.flatten_helper(cur.child)
            cur.next = cur_h
            cur_h.prev = cur
            cur_e.next = next
            next.prev = cur_e
            cur.child = None
        if cur.next:
            next_h, next_e = self.flatten_helper(next)
            return head, next_e
        return head, head


    def flatten(self, head):
        if head == None: return head
        return self.flatten_helper(head)[0]

    def nextLargerNodes(self, head):
        res = []
        if head == None: return []
        n = self.get_list_size(head)
        res = [0] * n
        import sys
        stack = [[sys.maxsize, -1]]
        cur = head
        idx = 0
        while cur:
            while stack[-1][0] < cur.val:
                top, top_idx = stack[-1]; stack.pop(-1)
                res[top_idx] = cur.val
            stack.append([cur.val, idx])
            idx += 1; cur = cur.next
        while len(stack) > 1:
            top, top_idx = stack[-1]; stack.pop(-1)
            res[top_idx] = 0
        return res

    def removeZeroSumSublists(self, head):
        if head == None: return head
        dummy = ListNode(-1)
        dummy.next = head
        pre = dummy; l = head
        while l:
            sum = 0
            r = l
            while r:
                sum += r.val
                if sum == 0:
                    pre.next = r.next
                    l = r
                    break
                r = r.next
            l = l.next
        return dummy.next





