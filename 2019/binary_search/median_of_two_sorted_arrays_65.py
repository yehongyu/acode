#coding=utf-8

class Solution:
    """
    @param: A: An integer array
    @param: B: An integer array
    @return: a double whose format is *.5 or *.0
    """

    # time: log(m+n)
    def findknum(self, A, B, k):
        if len(A) <= len(B):
            a1 = A
            a2 = B
        else:
            a1 = B
            a2 = A
        if len(a1) == 0:
            return a2[k-1]
        if k == 1:
            return a1[0] if a1[0] < a2[0] else a2[0]
        midi = min(k / 2, len(a1))
        midj = min(k - midi, len(a2))
        print(k, midi, midj, a1, a2)
        if a1[midi-1] < a2[midj-1]:
            return self.findknum(a1[midi:], a2, k-midi)
        elif a1[midi-1] > a2[midj-1]:
            return self.findknum(a1, a2[midj:], k-midj)
        else:
            return a1[midi-1]

    def findMedianSortedArrays(self, A, B):
        # write your code here
        m = len(A)
        n = len(B)
        if m + n <= 0:
            return -1
        total = m + n
        if total % 2 == 1:
            return self.findknum(A, B, (total+1)/2)
        else:
            return (self.findknum(A, B, total/2+1)
                + self.findknum(A, B, total/2)) / 2.0

s = Solution()

A = [1, 2, 3]
B = [4, 5]
print(s.findknum(A, B, 1))
A = [1, 2, 3]
B = [4, 5]
print(s.findMedianSortedArrays(A, B))
A = [1, 2, 3, 4, 5, 6]
B = [2, 3, 4, 5]
print(s.findMedianSortedArrays(A, B))
