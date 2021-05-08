# Definition for a binary tree node.
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):

    def bubbleSort(self, nums):
        """
        :type nums: list[int]
        :rtype: List[int]
        """
        size = len(nums)
        for i in range(size-1):
            for j in range(0,size-i-1):
                if nums[j] > nums[j+1]:
                    nums[j], nums[j+1] = nums[j+1], nums[j]
        return nums

    def quickSort_helper(self, nums, start, end):
        print("begin:", start, end)
        if start >= end: return
        mid = start + int((end-start)/2)
        val = nums[mid]
        if start != mid:
            nums[start], nums[mid] = nums[mid], nums[start]
            print('swap start', start, mid, nums)
        l = start; r = end
        while l < r:
            while l <= r and nums[l] <= val:
                l += 1
            while l <= r and nums[r] > val:
                r -= 1
            if l < r:
                nums[l], nums[r] = nums[r], nums[l]
                print('swap loop', l, r, nums)
        pos = l - 1
        if pos != start:
            nums[start], nums[pos] = nums[pos], nums[start]
            print('swap last',pos, start, nums)
        self.quickSort_helper(nums, 0, pos-1)
        self.quickSort_helper(nums, pos+1, end)


    def quickSort(self, nums):
        """
        :type nums: list[int]
        :rtype: List[int]
        """
        # mid, traverse, swap
        size = len(nums)
        self.quickSort_helper(
            nums, 0, size-1
        )
        return nums

    def mergeSort_helper(self, nums):
        size = len(nums)
        if size <= 1: return nums
        mid = int((size-1)/2)
        left = nums[0:mid+1]
        right = nums[mid+1:]

        # divide into two array
        sorted_left = self.mergeSort_helper(left)
        sorted_right = self.mergeSort_helper(right)

        # merge two sorted array
        arr = []
        i = 0; j = 0
        while i < len(sorted_left) and j < len(sorted_right):
            if sorted_left[i] <= sorted_right[j]:
                arr.append(sorted_left[i])
                i += 1
            else:
                arr.append(sorted_right[j])
                j += 1
        if i<len(sorted_left):
            arr.extend(sorted_left[i:])
        if j<len(sorted_right):
            arr.extend(sorted_right[j:])
        return arr


    def mergeSort(self, nums):
        """
        :type nums: list[int]
        :rtype: List[int]
        """
        size = len(nums)
        if size <= 1: return nums
        res = self.mergeSort_helper(nums)
        return res


    def heapSort(self, nums):
        """
        :type nums: list[int]
        :rtype: List[int]
        """
        # build: for i in range(n): addjustHeap(new tail)
        # get: return top, swap(top, tail), addjustHeadp(tail)




    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # mid, part, merge two sorted list,


if __name__ == "__main__":
    s = Solution()
    nums = [8,5,1,3,9,6,-2]
    print("origin nums:", nums)
    #res = s.bubbleSort(nums)
    #res = s.quickSort(nums)
    res = s.mergeSort(nums)
    print("sort:", res)