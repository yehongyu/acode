#coding=utf-8
import functools

def compare_func(a, b):
    if a[1] < b[1]:
        return -1
    if a[1] > b[1]:
        return 1
    if a[1] == b[1] and a[0] < b[0]:
        return -1
    if a[1] == b[1] and a[0] > b[0]:
        return 1
    return 0

class Solution(object):
    def scheduleCourse(self, courses):
        """
        :type courses: List[List[int]]
        :rtype: int
        """
        courses = sorted(courses, key=functools.cmp_to_key(compare_func))
        print(courses)
        from queue import PriorityQueue
        queue = PriorityQueue()
        cur = 0

        max_n = 0
        for i in range(len(courses)):
            time, dl = courses[i]
            if cur + time <= dl:
                cur += time
                queue.put(-time)
                print('if put', i, time, cur)
            elif queue.qsize() > 0:
                t = -queue.get()
                print('get', i, t)
                if t > time:
                    cur += time - t
                    queue.put(-time)
                    print('put', i, time, cur)
                else:
                    queue.put(-t)
                    print('put', i, t, cur)
        return queue.qsize()




s = Solution()
nums = [[100, 200], [200, 1300], [1000, 1250], [2000, 3200]]
nums = [[5, 5], [4, 6], [2, 6]]
nums = [[7,16],[2,3],[3,12],[3,14],[10,19],[10,16],[6,8],[6,11],[3,13],[6,16]]
print(s.scheduleCourse(nums))
