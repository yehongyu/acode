class Solution:
    """
    @param A: an array
    @param B: an array
    @return: the minimum number of swaps to make both sequences strictly increasing
    """
    def minSwap(self, A, B):
        # Write your code here
        if len(A) != len(B): return -1
        n = len(A)
        swap = [n] * n
        swap[0] = 1
        noswap = [n] * n
        noswap[0] = 0
        for i in range(1, n):
            if A[i-1] < A[i] and B[i-1] < B[i]:
                swap[i] = swap[i-1] + 1
                noswap[i] = noswap[i-1]
            if A[i-1] < B[i] and B[i-1] < A[i]:
                swap[i] = min(swap[i], noswap[i-1] + 1)
                noswap[i] = min(noswap[i], swap[i-1])
        return min(swap[n-1], noswap[n-1])



s = Solution()
A = [1,3,5,4]
B = [1,2,3,7]
A = [2,4,5,7,10]
B = [1,3,4,5,9]
A = [3,5,6,9,14,15,15,18,17,20]
B = [3,4,5,8,10,14,17,16,19,19]
print(s.minSwap(A, B))
