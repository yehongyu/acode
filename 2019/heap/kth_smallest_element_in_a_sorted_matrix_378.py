class Solution(object):
    def kthSmallest(self, matrix, k):
        n = len(matrix)
        if k <= 0 or k > n*n: return None
        if k == 0: return matrix[0][0]
        if k == n * n: return matrix[n-1][n-1]
        heap = []
        import heapq
        visited = set()
        visited.add(0)
        heapq.heappush(heap, [matrix[0][0], 0, 0])
        i = 0
        while i < k and len(heap)>0:
            top, idx, idy = heapq.heappop(heap)
            i += 1
            if i == k: return top
            if idx+1<n:
                id = (idx+1) * n + idy
                if id not in visited:
                    visited.add(id)
                    heapq.heappush(heap, [matrix[idx+1][idy], idx+1, idy])
            if idy+1<n:
                id = (idx) * n + idy+1
                if id not in visited:
                    visited.add(id)
                    heapq.heappush(heap, [matrix[idx][idy+1], idx, idy+1])
            print('loop', i, top, heap)
        return None

s = Solution()
matrix = [
   [ 1,  5,  9],
   [10, 11, 13],
   [12, 13, 15]
]
k = 8
matrix=[[1,3,5],[6,7,12],[11,14,14]]
k=6
k=3
print(s.kthSmallest(matrix, k))









