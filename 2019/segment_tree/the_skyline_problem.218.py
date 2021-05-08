#coding=utf-8

from Queue import PriorityQueue
from max_heap import MaxHeap
class Solution(object):
    def getSkyline(self, buildings):
        """
        :type buildings: List[List[int]]
        :rtype: List[List[int]]
        """
        if len(buildings) <= 0:
            return
        data = [[build[0], build[2], 0] for build in buildings]
        data += [[build[1], build[2], 1] for build in buildings]
        data = sorted(data, key = lambda x:(x[0], x[1]))
        print data
        heap = MaxHeap()
        print heap.size()
        result = []
        for item in data:
            x, h, tag = item[0:]
            pre_height = -heap.top() if heap.size() > 0 else 0
            if tag == 0:
                heap.add(-h) #top is the lowest height
                print 'push', -h
            else:
                print 'pop', heap.top()
                heap.pop() #pop the lowest height
            cur_height = -heap.top() if heap.size() > 0 else 0
            if tag == 0 and cur_height > pre_height:
                result.append([x, h])
            elif tag == 1 and h > cur_height:
                result.append([x, cur_height])
            print item, pre_height, cur_height, result
        return result




if __name__ == '__main__':
    buildings = [ [2, 9, 10], [3, 7, 15], [5, 12, 12], [15, 20, 10], [19, 24, 8] ]
    solu = Solution()
    print solu.getSkyline(buildings)


