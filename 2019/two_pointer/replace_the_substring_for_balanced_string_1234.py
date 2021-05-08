
from functools import cmp_to_key
def cmp(a, b):
    return a[0] - b[0]

class Solution(object):
    def balancedString(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        avg = n // 4
        cnt_map = {}
        for ch in s:
            if ch not in cnt_map:
                cnt_map[ch] = 0
            cnt_map[ch] += 1
        l = 0; r = 0;
        while r < n:
            ch = s[r]
            cnt_map[ch] -= 1
            need_move_left = True
            for ch in cnt_map.keys():
                if cnt_map[ch] > avg:
                    need_move_left = False
                    break
            while need_move_left and l < n:
                cnt_map[s[l]] += 1

    def numRescueBoats(self, people, limit):
        n = len(people)
        res = 0
        people = sorted(people)
        l = 0; r = n - 1
        while l < r:
            sum = people[l] + people[r]
            if sum <= limit:
                l += 1; r -= 1
                res += 1
            elif sum > limit:
                r -= 1
                res += 1
        if l==r:
            res += 1
        return res


    def maxProfitAssignment(self, difficulty, profit, worker):
        jobs = []
        for i in range(len(difficulty)):
            jobs.append([difficulty[i], profit[i]])
        jobs = sorted(jobs, key=cmp_to_key(cmp))
        print(jobs)
        n = len(jobs)
        worker = sorted(worker)
        print(worker)
        max_profit = 0; j = 0
        res = 0
        for i in range(len(worker)):
            while j < n and worker[i] >= jobs[j][0]:
                max_profit = max(jobs[j][1], max_profit)
                j += 1
            res += max_profit
        return res


s = Solution()
difficulty = [2,4,6,8,10]
profit = [10,20,30,40,50];
worker = [4,5,6,7]
print(s.maxProfitAssignment(difficulty, profit, worker))

'''
people = [1,3,2,2]
limit = 3
people = [3,5,3,4]
limit = 5
print(s.numRescueBoats(people, limit))
'''
