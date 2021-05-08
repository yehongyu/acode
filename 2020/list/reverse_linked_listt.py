# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

"""
# Definition for a Node.
"""
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    # Reverse a singly linked list.
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None: return head
        pre = None
        cur = head
        while cur:
            next = cur.next
            cur.next = pre
            pre = cur
            cur = next
        return pre

    def middleOfList(self, head):
        if head == None or head.next == None: return head
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next
            if fast: fast = fast.next
            else: break
        return slow

    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        if head == None or head.next == None: return head
        less = ListNode(-1); pre1 = less
        greater = ListNode(-1); pre2 = greater
        cur = head
        while cur:
            if cur.val < x:
                pre1.next = cur
                pre1 = cur
            else:
                pre2.next = cur
                pre2 = cur
            cur = cur.next
        pre1.next = greater.next
        pre2.next = None
        return less.next

    def hasCycle(self, head):
        slow = ListNode(-1); slow.next = head
        fast = ListNode(-1); fast.next = head
        cur = head
        while slow and fast and slow != fast:
            slow = slow.next
            fast = fast.next
            if fast: fast = fast.next
        if not slow or not fast:
            return False
        return True

    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        slow = ListNode(-1); slow.next = head
        fast = ListNode(-1); fast.next = head
        while slow and fast and slow != fast:
            slow = slow.next
            fast = fast.next
            if fast: fast = fast.next
        print("slow:", slow.val)
        if not slow or not fast:
            return None
        cur = ListNode(-1); cur.next = head
        while slow != cur:
            print("slow:", slow.val, ", cur:", cur.val)
            cur = cur.next
            slow = slow.next
        return slow

    def copyRandomList_withMap(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if head == None: return head
        node_map = {}
        cur = head
        while cur:
            new_node = Node(cur.val)
            node_map[cur] = new_node
            cur = cur.next
        cur = head
        while cur:
            new_node = node_map[cur]
            if cur.next:
                new_node.next = node_map[cur.next]
            if cur.random:
                new_node.random = node_map[cur.random]
        return node_map[head]

    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if head == None: return head
        cur = head
        while cur:
            new_node = Node(cur.val)
            next = cur.next
            cur.next = new_node
            new_node.next = next
            cur = next
        cur = head
        while cur:
            new_node = cur.next
            if cur.random:
                new_node.random = cur.random.next
            cur = cur.next.next
        new_head = head.next; cur=head
        while cur and cur.next:
            old_node = cur
            new_node = cur.next
            old_node.next = old_node.next.next
            if new_node.next:
                new_node.next = new_node.next.next
            else:
                new_node.next = None
            cur = old_node.next
        return new_head

    def isSubPath_is_list_start(self, head, root):
        if head == None or root == None: return False
        if head.val != root.val:
            return False
        if head.next:
            if root.left:
                res = self.isSubPath_is_list_start(head.next, root.left)
                if res: return True
            if root.right:
                return self.isSubPath_is_list_start(head.next, root.right)
            return False
        else:
            return True

    def isSubPath(self, head, root):
        """
        :type head: ListNode
        :type root: TreeNode
        :rtype: bool
        """
        if root == None or head == None:return False
        if head.val == root.val:
            if self.isSubPath_is_list_start(head, root):
                return True
        if self.isSubPath(head, root.left):
            return True
        return self.isSubPath(head, root.right)

    # 1171. Remove Zero Sum Consecutive Nodes from Linked List
    # [1,2,-3,3,1] ==> [3,1]
    def removeZeroSumSublists(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None: return head
        dummy = ListNode(0); dummy.next = head
        node_map = {0: dummy}
        acc_sum = 0; cur = head;
        while cur:
            acc_sum += cur.val
            print(cur.val, acc_sum)
            if acc_sum not in node_map:
                node_map[acc_sum] = cur
            else:
                pre = node_map[acc_sum]
                detete_node = pre.next
                tmp_sum = acc_sum
                while detete_node != cur:
                    tmp_sum += detete_node.val
                    node_map.pop(tmp_sum)
                    detete_node = detete_node.next
                pre.next = cur.next
            cur = cur.next
        return dummy.next

    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        from queue import PriorityQueue
        queue = PriorityQueue()
        for head in lists:
            queue.put((head.val, head)) # value=(priority, data)
        dummy = ListNode(-1)
        cur = dummy
        while queue.qsize() > 0:
            value = queue.get()
            print(value)
            node = value[1]
            cur.next = node
            if node.next:
                queue.put((node.next.val, node.next))
            cur = cur.next
        cur.next = None
        return dummy.next

    def deleteContinousSumZeroFromList(self, head):
        if head == None:
            return None
        nmap = {}
        dummy = ListNode(0)
        dummy.next = head; cur = head
        acc = 0; nmap[0] = dummy
        while cur:
            acc += cur.val
            next = cur.next
            if nmap.get(acc):
                pre = nmap[acc]; p1 = pre.next
                tmp = acc
                while p1 != cur:
                    tmp += p1.val
                    nmap.pop(tmp)
                    p1 = p1.next
                pre.next = next
            nmap[acc] = cur
            cur = next
        return dummy.next




def show_list(head):
    cur = head
    while cur:
        print(cur.val, '->', end="")
        cur = cur.next
    print("endl")

if __name__ == '__main__':
    s = Solution()

    # [1,3,2,-3,-2,5,5,-5,1]
    #head = ListNode(0)
    #head.next = ListNode(0)
    head = ListNode(1)
    head.next = ListNode(3)
    head.next.next = ListNode(2)
    head.next.next.next = ListNode(-3)
    head.next.next.next.next = ListNode(-2)
    head.next.next.next.next.next = ListNode(5)
    head.next.next.next.next.next.next = ListNode(5)
    head.next.next.next.next.next.next.next = ListNode(-5)
    head.next.next.next.next.next.next.next.next = ListNode(1)

    res = s.deleteContinousSumZeroFromList(head)
    show_list(res)
    #res = s.reverseList(head)
    #res = s.middleOfList(head)
    #res = s.partition(head, 2)
    #res = s.hasCycle(head)
    #res = s.detectCycle(head)
    #print('list res:', res.val)
    #res = s.removeZeroSumSublists(head)
    '''
    head1 = ListNode(1); head1.next = ListNode(3)
    head2 = ListNode(2); head2.next = ListNode(4)
    res = s.mergeKLists([head1, head2])
    show_list(res)

    root = TreeNode(1)
    root.left = TreeNode(4)
    #root.left.left = TreeNode(4)
    root.left.right = TreeNode(2)
    root.left.right.left = TreeNode(1)

    root.right = TreeNode(4)
    root.right.left = TreeNode(2)
    root.right.left.left = TreeNode(6)
    root.right.left.right = TreeNode(8)
    root.right.left.right.left = TreeNode(1)
    root.right.left.right.right = TreeNode(3)

    #res = s.isSubPath(head, root)
    #print(res)
    '''
