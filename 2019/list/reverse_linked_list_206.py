# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        pre = None
        cur = head
        while cur != None:
            next = cur.next
            cur.next = pre
            pre = cur
            cur = next
        return pre

    def reverseBetween(self, head, m, n):
        if m <= 0 or m >= n:
            return head
        dummy = ListNode(-1)
        dummy.next = head
        cur = dummy
        i = 0
        pre = cur
        pre_m = cur
        while cur != None:
            pre = cur
            cur = cur.next
            i += 1
            if i == m:
                m_node = cur
                pre_m = pre
            if i == n:
                n_node = cur
                break
        post_n = n_node.next
        n_node.next = None
        self.reverseList(m_node)
        pre_m.next = n_node
        m_node.next = post_n
        return dummy.next

    def mergeTwoLists(self, l1, l2):
        dummy = ListNode(-1)
        cur = dummy
        while l1 != None and l2 != None:
            if l1.val <= l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next
        if l1 != None:
            cur.next = l1
        if l2 != None:
            cur.next = l2
        return dummy.next

    def partition(self, head, x):
        h1 = ListNode(-1)
        h2 = ListNode(-1)
        l1 = h1; l2 = h2
        l1_end = h1; l2_end = h2
        cur = head
        while cur != None:
            if cur.val < x:
                l1_end = cur
                l1.next = cur
                l1 = l1.next
            else:
                l2_end = cur
                l2.next = cur
                l2 = l2.next
            cur = cur.next
        l1_end.next = h2.next
        l2_end.next = None
        return h1.next

    def insertNodeInSortedList(self, head, x):
        dummy = ListNode(-1)
        dummy.next = head
        cur = dummy
        while cur.next != None and cur.next.val <= x:
            cur = cur.next
        post = cur.next
        cur.next = ListNode(x)
        cur.next.next = post
        return dummy.next

    def removeNodeInSortedList(self, head, x):
        dummy = ListNode(-1)
        dummy.next = head
        cur = dummy
        while cur.next != None:
            if cur.next.val == x:
                post = cur.next.next
                cur.next = post
            else:
                cur = cur.next
        return dummy.next

    def middleNode(self, head):
        dummy = ListNode(-1)
        dummy.next = head
        slow = dummy
        fast = dummy
        while fast != None:
            slow = slow.next
            fast = fast.next
            if fast != None:
                fast = fast.next
        return slow

    def middleNodeReturnLeftEnd(self, head):
        dummy = ListNode(-1)
        dummy.next = head
        slow = dummy
        fast = dummy
        pre = dummy
        while fast != None:
            pre = slow
            slow = slow.next
            fast = fast.next
            if fast != None:
                fast = fast.next
            else:
                return pre
        return pre

    def mergeSortList(self, head):
        if head == None or head.next == None:
            return head
        mid = self.middleNodeReturnLeftEnd(head)
        r_h = mid.next
        mid.next = None
        left = self.mergeSortList(head)
        right = self.mergeSortList(r_h)
        return self.mergeTwoLists(left, right)


    def partitionToTwoList(self, head, x):
        h1 = ListNode(-1)
        h2 = ListNode(-1)
        l1 = h1; l2 = h2
        l1_end = h1; l2_end = h2
        cur = head
        while cur != None:
            if cur.val < x:
                l1_end = cur
                l1.next = cur
                l1 = l1.next
            else:
                l2_end = cur
                l2.next = cur
                l2 = l2.next
            cur = cur.next
        l1_end.next = None
        l2_end.next = None
        return h1.next, h2.next

    def quickSortList(self, head):
        if head == None or head.next == None:
            return head
        pre_mid = self.middleNodeReturnLeftEnd(head)
        mid = pre_mid.next
        pre_mid.next = mid.next
        mid.next = None
        key = mid.val
        show_list(head, "head: ")
        l1, l2 = self.partitionToTwoList(head, key)
        show_list(l1, "l1: ")
        show_list(l2, "l2: ")
        sl1 = self.quickSortList(l1)
        sl2 = self.quickSortList(l2)
        dummy = ListNode(-1)
        dummy.next = sl1; tmp = dummy
        while tmp.next != None:
            tmp = tmp.next
        tmp.next = mid
        return self.mergeTwoLists(dummy.next, sl2)

    def mergeNoSortedList(self, l1, l2):
        dummy = ListNode(-1)
        cur = dummy
        flag = True
        while l1 != None or l2 != None:
            if flag:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            flag = not flag
            cur = cur.next
        return dummy.next

    def reorderList(self, head):
        if head == None or head.next == None or head.next.next == None:
            return head
        left_end = self.middleNodeReturnLeftEnd(head)
        right_head = left_end.next
        left_end.next = None
        right = self.reverseList(right_head)
        return self.mergeNoSortedList(head, right)

    def removeNthFromEnd(self, head, n):
        if head == None or n == 0:
            return head
        if head.next == None:
            return None if n == 1 else head
        dummy = ListNode(-1)
        dummy.next = head
        p1 = dummy
        p2 = dummy
        i = 0
        while i < n and p1 != None:
            i += 1
            p1 = p1.next
        if p1 == None:
            return head
        while p1.next != None:
            p1 = p1.next
            p2 = p2.next
        p2.next = p2.next.next
        return dummy.next

    def hasCycle(self, head):
        if head == None:
            return False
        if head.next == head:
            return True
        dummy = ListNode(-1)
        dummy.next = head
        slow = dummy.next
        fast = dummy.next.next
        while fast != None and fast != slow:
            fast = fast.next
            if fast != None:
                fast = fast.next
            slow = slow.next
        if fast == slow:
            return True
        else:
            return False

    def detectCycle(self, head):
        if head == None:
            return None
        if head.next == head:
            return head
        dummy = ListNode(-1)
        dummy.next = head
        slow = dummy.next
        fast = dummy.next.next
        while fast != None and fast != slow:
            fast = fast.next
            if fast != None:
                fast = fast.next
            slow = slow.next
        if fast != slow:
            return None
        slow = dummy
        while slow != fast:
            slow = slow.next
            fast = fast.next
        return slow

    def mergeKLists(self, lists):
        dummy = ListNode(-1)
        k = len(lists)
        if k == 0:
            return None
        if k == 1:
            return lists[0]
        from queue import PriorityQueue
        queue = PriorityQueue(k)
        for i in range(k):
            h = lists[i]
            queue.put((h.val, i))
        cur = dummy
        while not queue.empty():
            val, idx = queue.get()
            l = lists[idx]
            cur.next = l
            cur = cur.next
            lists[idx] = l.next
            if l.next != None:
                queue.put((l.next.val, idx))
        return dummy.next

    """
    @param: head: The first node of linked list.
    @return: a tree node
    """
    def sortedListToBST_middleNode(self, head):
        # write your code here
        if head == None:
            return None
        if head.next == None:
            return TreeNode(head.val)
        mid_pre = self.middleNodeReturnLeftEnd(head)
        mid = mid_pre.next
        node = TreeNode(mid.val)
        l1 = head
        l2 = mid.next
        mid_pre.next = None
        print('mid:', mid.val)
        show_list(l1, 'l1:')
        show_list(l2, 'l2:')
        node.left = self.sortedListToBST(l1)
        node.right = self.sortedListToBST(l2)
        return node

    def convertListToArray(self, head):
        arr = []
        cur = head
        while cur != None:
            arr.append(cur.val)
            cur = cur.next
        return arr

    def sortedListToBSTHelper(self, arr, start, end):
        if start > end:
            return None
        if start == end:
            return TreeNode(arr[start])
        mid = start + int((end-start)/2)
        node = TreeNode(arr[mid])
        node.left = self.sortedListToBSTHelper(arr, start, mid-1)
        node.right = self.sortedListToBSTHelper(arr, mid+1, end)
        return node


    def sortedListToBST_array(self, head):
        arr = self.convertListToArray(head)
        print(arr)
        return self.sortedListToBSTHelper(arr, 0, len(arr)-1)

    def getlistLen(self, head):
        res = 0
        cur = head
        while cur != None:
            res += 1
            cur = cur.next
        return res

    def sortedListToBST_DC_helper(self, cur, size):
        if size <= 0 or cur == None:
            return None, cur
        left, cur = self.sortedListToBST_DC_helper(cur, size//2)
        root = TreeNode(cur.val)
        cur = cur.next
        right, cur = self.sortedListToBST_DC_helper(cur, size-1-(size//2))
        root.left = left
        root.right = right
        return root, cur

    def sortedListToBST_DC(self, head):
        if head == None:
            return None
        if head.next == None:
            return TreeNode(head.val)
        size = self.getlistLen(head)
        return self.sortedListToBST_DC_helper(head, size)[0]


def show_list(head, pre=' '):
    cur = head
    print(pre, end='')
    while cur != None:
        print(cur.val, '->', end=' ')
        cur = cur.next
    print('end')

def show_tree(root, pre=' '):
    if root == None:
        return
    print(pre, end='')
    queue = []
    queue.append(root)
    while len(queue) > 0:
        size = len(queue)
        for i in range(size):
            node = queue[0]
            queue.pop(0)
            print(node.val, '-', end='')
            if node.left != None:
                queue.append(node.left)
            if node.right != None:
                queue.append(node.right)
        print('end')

head = ListNode(-1)
head.next = ListNode(0)
head.next.next = ListNode(2)
#head.next.next.next = ListNode(9)
#head.next.next.next.next = ListNode(10)
#head.next.next.next.next.next = ListNode(15)
#head.next.next.next.next.next.next = ListNode(25)

s = Solution()
#show_list(head)
#show_list(s.partition(head, 4))
#show_list(s.insertNodeInSortedList(ListNode(1), 19))
#show_list(s.removeNodeInSortedList(head, 12))
#show_list(s.middleNode(ListNode(1)))
#show_list(s.mergeSortList(head))
#show_list(s.quickSortList(head))
#show_list(s.reorderList(head))
#l1, l2 = s.partitionToTwoList(head, 12)
#show_list(l1)
#show_list(l2)
#show_list(s.removeNthFromEnd(head, 6))
#show_list(s.mergeKLists([head, head2, head3]))

tree = s.sortedListToBST_DC(head)
print(tree, tree.val)
show_tree(tree)

