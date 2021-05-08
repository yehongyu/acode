'''
Logic:
We can create a reminder frequency map.
1. First, we get reminder of each num.
2. then we need a number which's reminder is k-reminder(num).
3. if comple=k-reminder(num) is in freq, then we can minus 1 to this freq[comple];
it means we find a number which can consit a pair with current number,
and the sum of the pair is divisible by k.
4. if comple is no in freq, or freq[comple] is 0, then we add 1 to freq[reminder(num)].
5. At last, if all val in freq is 0, then all num in array has been into a pair with
other number, return True; or return False.


'''

class Solution(object):
    def canArrange(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: bool
        """
        if len(arr) % 2 != 0 or k == 0: return False
        freq = {}
        for num in arr:
            val = num % k
            comple = (k-val) % k
            if comple in freq and freq[comple]>0:
                freq[comple] -= 1
            elif val not in freq:
                freq[val] = 1
            else:
                freq[val] += 1
            print(num, val, comple, freq)
        print(freq)
        for k, v in freq.items():
            if v != 0: return False
        return True

s = Solution()
arr = [1,2,3,4,5,10,6,7,8,9]; k = 5 # res=True
arr = [1,2,3,4,5,6]; k = 7 # True
arr = [1,2,3,4,5,6]; k = 10 # False
arr = [-10,10]; k = 2 # True
arr = [-1,1,-2,2,-3,3,-4,4]; k = 3 # True
arr = [-4,-7,5,2,9,1,10,4,-8,-3]; k = 3
res = s.canArrange(arr, k)
print(res)