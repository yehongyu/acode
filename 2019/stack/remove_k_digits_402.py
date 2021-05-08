class Solution(object):
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        n = len(num)
        if n <= k: return '0'
        stack = []
        for c in num:
            c = int(c)
            while k > 0 and len(stack) > 0 and stack[-1] > c:
                k -= 1
                stack.pop(-1)
            stack.append(c)
            print(c, stack)
        while k > 0 and len(stack) > 0:
            k -= 1
            stack.pop(-1)
        print(stack)
        res = ''.join(map(str, stack))
        i = 0
        while i < len(res) and res[i] == '0': i += 1
        return res[i:] if i < len(res) else '0'

    def find132pattern(self, nums):
        n = len(nums)
        stack = []
        import sys
        second = -sys.maxsize-1
        for i in range(n-1, -1, -1):
            print(i, nums[i], second, stack)
            if nums[i] < second: return True
            while len(stack) > 0 and stack[-1] < nums[i]:
                second = stack[-1]; stack.pop(-1)
            stack.append(nums[i])
        return False

    def nextGreaterElement_backward(self, nums1, nums2):
        m = len(nums1)
        n = len(nums2)
        map = {}
        stack = []
        for i in range(n-1, -1, -1):
            while len(stack) > 0 and nums2[i] > stack[-1]:
                stack.pop(-1)
            map[nums2[i]] = stack[-1] if len(stack) > 0 else -1
            stack.append(nums2[i])
        res = []
        for val in nums1:
            res.append(map[val])
        return res

    def nextGreaterElement(self, nums1, nums2):
        m = len(nums1)
        n = len(nums2)
        map = {}
        for val in nums2:
            map[val] = -1
        stack = []
        for i in range(0, n):
            while len(stack) > 0 and nums2[i] > nums2[stack[-1]]:
                top = stack[-1]
                stack.pop(-1)
                map[nums2[top]] = nums2[i]
            stack.append(i)
        res = []
        for val in nums1:
            res.append(map[val])
        return res

    def nextGreaterElements(self, nums):
        n = len(nums)
        res = [-1] * n
        stack = []
        for i in range(0, n):
            while len(stack) > 0 and nums[i] > nums[stack[-1]]:
                top = stack[-1]
                stack.pop(-1)
                res[top] = nums[i]
            stack.append(i)
        for i in range(0, n):
            while len(stack) > 0 and nums[i] > nums[stack[-1]]:
                top = stack[-1]
                stack.pop(-1)
                res[top] = nums[i]
        return res

    def exclusiveTime(self, n, logs):
        if n <= 0 or len(logs) % 2 != 0: return []
        res = [0] * n
        stack = []
        for log in logs:
            vals = log.split(':')
            if vals[1] == 'start':
                stack.append([int(vals[0]), vals[1], int(vals[2])])
            else:
                cur = int(vals[2])
                while len(stack) > 0 and stack[-1][1] == 'child':
                    top = stack[-1]; stack.pop(-1)
                    cur -= top[2]
                if len(stack) > 0 and stack[-1][1] == 'start':
                    top = stack[-1]; stack.pop(-1)
                    cur -= top[2]
                    res[int(vals[0])] += cur + 1
                    print(stack)
                stack.append([int(vals[0]), 'child', int(vals[2])-top[2]+1])
            print(log, stack, res)
        return res

    def removeDuplicates(self, S):
        """
        :type S: str
        :rtype: str
        """
        stack = []
        for s in S:
            if stack and s == stack[-1]:
                stack.pop()
                continue
            stack.append(s)
            print(s, stack)
        return "".join(stack)


s = Solution()
sss = "abbbaca"

print(s.removeDuplicates(sss))
'''
logs = ["0:start:0","1:start:2","1:end:5","0:end:6"]
logs = ["0:start:0","0:start:2","0:end:5","0:start:6","0:end:6","0:end:7"]
print(s.exclusiveTime(1, logs))
print(s.nextGreaterElements([1,2,1]))
nums1 = [4,1,2]; nums2 = [1,3,4,2]
print(s.nextGreaterElement(nums1, nums2))
'''

#print(s.find132pattern([-1, 5, -2, 3, -2]))
#print(s.find132pattern([-2, 1, 2, -2, 1, 2]))

#print(s.removeKdigits('10200', 1))
#print(s.removeKdigits('10', 1))
#print(s.removeKdigits('112', 1))
