class Solution(object):
    def validateBinaryTreeNodes(self, n, leftChild, rightChild):
        """
        :type n: int
        :type leftChild: List[int]
        :type rightChild: List[int]
        :rtype: bool
        """
        if n <= 0: return True
        indegree = {}
        for i in range(n):
            left = leftChild[i]
            if left != -1:
                if left not in indegree:
                    indegree[left] = 0
                indegree[left] += 1
            right = rightChild[i]
            if right != -1:
                if right not in indegree:
                    indegree[right] = 0
                indegree[right] += 1
        queue = []
        visited = [False] * n
        for i in range(n):
            if i not in indegree:
                visited[i] = True
                queue.append(i)
            elif indegree[i] > 1: return False
        if len(queue) != 1: return False
        while len(queue):
            qlen = len(queue)
            for i in range(qlen):
                cur = queue[0]; queue.pop(0)
                if leftChild[cur] != -1:
                    if not visited[leftChild[cur]]:
                        visited[leftChild[cur]] = True
                        queue.append(leftChild[cur])
                    else: return False
                if rightChild[cur] != -1:
                    if not visited[rightChild[cur]]:
                        visited[rightChild[cur]] = True
                        queue.append(rightChild[cur])
                    else: return False
        for i in range(n):
            if not visited[i]: return False
        return True


s = Solution()
n = 4
leftChild = [1,2,0,-1]
rightChild = [-1,-1,-1,-1]
print(s.validateBinaryTreeNodes(
    n, leftChild, rightChild
))
