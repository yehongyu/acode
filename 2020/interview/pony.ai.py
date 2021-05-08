def func(points):
    size = len(points)
    if size < 3: return []
    src = points[0]
    distance = [0]
    min_dist = sys.maxsize
    min_dist_pos = -1
    for i in range(1, size):
        cur_dist = pow(points[i][0] - points[0][0], 2) + pow(points[i][1] - points[0][1], 2)
        distance.append(cur_dist)
        if cur_dist < min_dist:
            min_dist = cur_dist
            min_dist_pos = i

    # search one point: not int a line and nearest
    if points[min_dist_pos][0] - points[0][0] != 0:
        val = points[min_dist_pos][1] - points[0][1] / (points[min_dist_pos][0] - points[0][0])
    else:
        val = -1
    second_pos = -1
    second_pos_dist = sys.maxsize
    for i in range(1, size):
        if i == min_dist_pos: continue
        if points[i][0] == points[min_dist_pos][0] and points[i][1] == points[min_dist_pos][1]: continue
        if points[i][0] - points[0][0] != 0:
            tmp1 = points[i][1] - points[0][1] / (points[i][0] - points[0][0])
        else:
            tmp1 = -1
        if tmp1 == val: continue
        if distance[i] < second_pos_dist:
            second_pos_dist = distance[i]
            second_pos = i
    res = []
    if second_pos != -1:
        res = [points[0], points[min_dist_pos], points[second_pos]]
    return res

'''
给定两棵二叉搜索树, 和一个目标数字S, 判断能否在两颗树中分别找到一个数, 使得其和为S.树的结构体定义如下:

struct
TreeNode
{
    int
val;
TreeNode * left;
TreeNode * right;
};

tree1
node.val: s - node.val
m * n
m * log(n)
map1: < val: >
map2: <>
O(2(m + n))
m + n + max(m, n)
'''



def convert_tree(root, res):
    if root == None: return
    convert_tree(root.left, res)
    res.add(root.val)
    convert_tree(root.right, res)


def helper(root, target_map, s):
    if root == None: return False
    if s - root.val in target_map:
        return True
    if helper(root.left, target_map, s):
        return True
    return helper(root.right, target_map, s)


def func(tree1, tree2, s):
    if tree1 == None or tree2 == None:
        return False
    nodes = set();
    convert_tree(tree1, nodes)
    res = helper(tree2, nodes, s)
    return res