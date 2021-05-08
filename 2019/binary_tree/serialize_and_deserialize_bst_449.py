# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        :type root: TreeNode
        :rtype: str
        """
        if root == None:
            return '#'
        l_path = self.serialize(root.left)
        r_path = self.serialize(root.right)
        path = ','.join([str(root.val), l_path, r_path])
        print(path)
        return path

    def des_helper(self, data, pos):
        if pos >= len(data): return None, pos
        if data[pos] == '#': return None, pos
        root = TreeNode(data[pos])
        root.left, end = self.des_helper(data, pos+1)
        print(end)
        root.right, end = self.des_helper(data, end+1)
        return root, end

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        :type data: str
        :rtype: TreeNode
        """
        if len(data) == 0: return None
        if data == '#': return None
        data = data.split(',')
        root, end = self.des_helper(data, 0)
        return root

def show_tree(root):
    if root == None: return
    queue = []
    queue.append(root)
    while len(queue) > 0:
        qlen = len(queue)
        for i in range(qlen):
            cur = queue[0]; queue.pop(0)
            print(cur.val, end=' ')
            if cur.left: queue.append(cur.left)
            if cur.right: queue.append(cur.right)
        print('endl')

codec = Codec()
root = TreeNode(1)
root.left = TreeNode(2)
root.left.right = TreeNode(4)
root.right = TreeNode(3)
data = codec.serialize(root)
print(data)
data = '41,37,24,1,0,#,#,2,#,4,3,#,#,9,7,6,5,#,#,#,8,#,#,11,10,#,#,16,15,12,#,13,#,14,#,#,#,19,18,17,#,#,#,20,#,22,21,#,#,23,#,#,35,30,29,26,25,#,#,27,#,28,#,#,#,32,31,#,#,34,33,#,#,#,36,#,#,39,38,#,#,40,#,#,44,42,#,43,#,#,48,46,45,#,#,47,#,#,49,#,#'
print('len:', len(data))
new_tree = codec.deserialize(data)
show_tree(new_tree)
