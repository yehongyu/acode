'''
Problem description:
Given a binary tree, return all duplicate subtrees.
For each kind of duplicate subtrees, you only need to
reeturn the root of any one of them.
Two trees are duplicate if they have the same structure
with same node values.


Solution:
We need to compare two subtree is same or not.
So we can transfer the subtree to a string based on the preorder,
and then compare the transfered string is equal or not.
For each node, we will get the transfered string of its left and right,
then we will conbine the value of current node with its left chars and right chars
as node's chars. If this node chars is in memory and the count of times of this chars
is 1, we will put this node into dup_list, as it means the subtree is same with
the previous subtree. If memory[chars] is greater than 1, it means we have added
the same subtree to dup_list, so we don't need to added the same subetree again.

'''



# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):

    def findDuplicateSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: List[TreeNode]
        """
        if root == None: return []
        dup_list = []
        memory = {}
        self.helper(dup_list, memory, root)
        return dup_list


    def helper(self, dup_list, memory, root):
        if root == None: return "#"
        left_chars = self.helper(dup_list, memory, root.left)
        right_chars = self.helper(dup_list, memory, root.right)
        chars = str(root.val) +","+ left_chars +","+ right_chars
        if chars not in memory:
            memory[chars] = 0
        elif memory[chars] == 1:
            dup_list.append(root)
        memory[chars] += 1
        return chars

s = Solution()
root = TreeNode(1)
root.left = TreeNode(2)
root.left.left = TreeNode(4)
root.right = TreeNode(3)
root.right.left = TreeNode(2)
root.right.left.left = TreeNode(4)
root.right.right = TreeNode(4)


res = s.findDuplicateSubtrees(root)
for node in res:
    print(node.val)