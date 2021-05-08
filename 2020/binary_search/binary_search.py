class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):

    def binarySearch(self, nums, val):
        """
        :type nums: list[int], sorted
        :rtype: index, int
        """
        size = len(nums)
        l = 0; r = size - 1
        while l <= r:
            mid = l + int((r-l)/2)
            print(l, mid, r)
            if nums[mid] == val:
                return mid
            elif val > nums[mid]:
                l = mid + 1
            elif val < nums[mid]:
                r = mid - 1
        return -1

    # confirm mid position, then compare target with mid and left or right value
    def searchInRotatedSortedArray(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        size = len(nums)
        l = 0; r = size - 1
        while l <= r:
            mid = l + int((r-l)/2)
            print(l, r, mid, nums)
            if nums[mid] == target: return mid
            if nums[l] <= nums[mid]:
                if nums[l] <= target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            else:
                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
        return -1

    def searchInRotatedSortedArrayDuplicate(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        size = len(nums)
        l = 0; r = size - 1
        while l <= r:
            mid = l + int((r-l)/2)
            print(l, r, mid, nums)
            if nums[mid] == target: return True
            if nums[l] < nums[mid]:
                if nums[l] <= target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            elif nums[l] > nums[mid]:
                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
            else:
                l += 1
        return False

    # InRotatedSortedArray: no duplicate
    def findMin11(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        size = len(nums)
        l = 0; r = size-1
        while l <= r:
            if nums[l] <= nums[r]: return nums[l]
            mid = l + int((r-l)/2)
            if nums[l] <= nums[mid]:
                l = mid + 1
            else:r = mid
        return None

    # InRotatedSortedArray: has duplicate
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        size = len(nums)
        l = 0; r = size-1
        while l < r:
            if nums[l] < nums[r]: return nums[l]
            mid = l + int((r-l)/2)
            print(l, r, mid, nums)
            if nums[l] < nums[mid]:
                l = mid + 1
            elif nums[l] > nums[mid]:
                r = mid
            else:l += 1
        if l == r: return nums[l]

    # nums = [0,0,0,1,1,1]
    def firstBadVersion(self, nums):
        """
        :type n: int
        :rtype: int
        """
        size = len(nums)
        if size == 0: return -1
        l = 0; r = size - 1
        while l < r:
            mid = l + int((r-l)/2)
            if nums[mid] == 1:
                r = mid
            elif nums[mid] == 0:
                l = mid + 1
        if nums[r] == 1: return r
        return -1


    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        size = len(nums)
        if size <= 0: return -1
        if size == 1: return 0
        l = 0; r = size-1
        while l+1 < r:
            mid = l + int((r-l)/2)
            if nums[mid-1] < nums[mid] < nums[mid+1]:
                l = mid + 1
            elif nums[mid-1] > nums[mid] > nums[mid+1]:
                r = mid - 1
            elif nums[mid-1] > nums[mid] < nums[mid+1]:
                r = mid - 1
            elif nums[mid-1] < nums[mid] > nums[mid+1]:
                return mid
        if nums[l] > nums[r]: return l
        else:return  r

    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x < 0: return -1
        if x in [0, 1]: return x
        l = 1; r = int(x/2)

        while l < r:
            mid = l + int((r-l)/2)
            square = mid * mid
            if square == x:
                return mid
            elif square > x:
                r = mid - 1
            elif square < x:
                l = mid + 1
        if l * l <= x: return l
        else: return l-1


    def myPow(self, x, n):
        """
        :type x: float
        :type n: int, maybe negative
        :rtype: float
        """
        if n == 0: return 1
        if x == 0: return 0
        if n < 0: return self.myPow(1/x, -n)
        if n == 1: return x
        next_n = int(n/2)
        val = self.myPow(x, next_n)
        val = val * val
        if n % 2 == 1:
            val = val * x
        return val



    def findKSortedArrays(self, nums1, i, nums2, j, k):
        m = len(nums1); n = len(nums2)
        if i > m-1: return nums2[j+k-1]
        if j > n-1: return nums1[i+k-1]
        if k == 1: return min(nums1[i], nums2[j])
        ni = min(i + int(k/2) - 1, m-1)
        num_1 = ni-i+1
        nj = min(j+ k-num_1-1, n-1)
        num_2 = nj-j+1
        if nums1[ni] < nums2[nj]:
            return self.findKSortedArrays(nums1, ni+1, nums2, j, k-num_1)
        else:
            return self.findKSortedArrays(nums1, i, nums2, nj+1, k-num_2)

    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        m = len(nums1)
        n = len(nums2)
        if (m + n) % 2 == 1:
            k = int((m+n+1)/2)
            return self.findKSortedArrays(nums1, 0, nums2, 0, k)
        else:
            k1 = int((m+n+1)/2)
            k2 = int((m+n+2)/2)
            return (self.findKSortedArrays(nums1, 0, nums2, 0, k1)
                    + self.findKSortedArrays(nums1, 0, nums2, 0, k2)) / 2

    def minOperations(self, nums, x):
        """
        :type nums: List[int]
        :type x: int
        :rtype: int
        """
        if len(nums) <= 0: return -1
        total = sum(nums)
        if total == x: return len(nums)
        target = total - x
        max_subarray_len = -1
        map = {}; acc = 0
        print("target:", target, len(nums))
        for i in range(len(nums)):
            acc += nums[i]
            key = acc - target
            if key in map:
                max_subarray_len = max(i-map[key], max_subarray_len)
                print("max:", max_subarray_len)
            elif acc not in map:
                map[acc] = i
            print(nums[i], acc, key, map)
        if max_subarray_len == -1: return -1
        else: return len(nums) - max_subarray_len

    def furthestBuilding(self, heights, bricks, ladders):
        """
        :type heights: List[int]
        :type bricks: int
        :type ladders: int
        :rtype: int
        """
        import heapq
        heap = []
        for i in range(1, len(heights)):
            if heights[i] <= heights[i-1]: continue
            cnt = heights[i] - heights[i-1]
            heapq.heappush(heap, cnt)
            if len(heap) > ladders:
                bricks -= heapq.heappop(heap)
            if bricks < 0:
                return i-1
        return len(heights) -1

    def find_duplicate_helper(self, root, mem, res):
        if root == None: return "#"
        left_str = self.find_duplicate_helper(root.left, mem)
        right_str = self.find_duplicate_helper(root.left, mem)
        new_str = ",".join(str(root.val), left_str, right_str)
        if new_str in mem:
            if mem[new_str] == 1:
                res.append(root)
            mem[new_str] += 1
        else:
            mem[new_str] = 1
        return new_str

    def findDuplicate(self, root):
        if root == None: return []
        mem = {}; res = []
        self.find_duplicate_helper(root, mem, res)
        return res


if __name__ == "__main__":
    s = Solution()
    nums = [0,3,4,7,9,12,23,35]
    #res = s.binarySearch(nums, 35)

    nums = [-3,-3,9,12,23,35,-3,-3,-3,-3]
    nums = [2,2,2,0,1]
    #res = s.searchInRotatedSortedArray(nums, 7)
    #res = s.findMin(nums)
    nums = [1,1,1,1,1]
    #res = s.searchInRotatedSortedArray(nums, 7)
    #res = s.firstBadVersion(nums)
    nums = [9,7,4,3,2,1,4]
    #res = s.findPeakElement(nums)
    #res = s.mySqrt(10)
    res = s.myPow(2, -4)
    nums1 = [1,2]
    nums2 = [3,4]
    #res = s.findMedianSortedArrays(nums1, nums2)
    #print('pow=', res)

    nums = [1,1,4,2,3]; x=5 # 2
    nums = [5,6,7,8,9]; x =4 # -1
    nums = [3,2,20,1,1,3]; x=10 # 5
    nums = [8828,9581,49,9818,9974,9869,9991,10000,10000,10000,9999,9993,9904,8819,1231,6309]
    x = 134365
    res = s.minOperations(nums, x)
    print('pow=', res)
