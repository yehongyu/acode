
class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

class Solution(object):

    def constructMaxTree(self, nums):
        n = len(nums)
        if n == 0:
            return None
        if n == 1:
            return TreeNode(nums[0])
        stack = []
        for i in range(n+1):
            if i == n:
                while len(stack) > 0:
                    node = stack[-1]
                    stack.pop(-1)
                    if len(stack) > 0:
                        stack[-1].right = node
                    else:
                        return node
                continue
            if len(stack) == 0 or nums[i] <= stack[-1].val:
                node = TreeNode(nums[i])
                stack.append(node)
            else:
                new_node = TreeNode(nums[i])
                while len(stack) > 0 and nums[i] > stack[-1].val:
                    cur = stack[-1]
                    stack.pop(-1)
                    if len(stack) > 0 and stack[-1].val > cur.val and not (stack[-1].val > nums[i]):
                        stack[-1].right = cur
                    else:
                        new_node.left = cur
                stack.append(new_node)

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


s = Solution()
res = s.constructMaxTree([2, 1, 5, 6, 0, 3])
show_tree(res, 'tree:')
