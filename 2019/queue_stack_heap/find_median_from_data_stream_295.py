class MedianFinder(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        from queue import PriorityQueue # min_heap
        self.max_heap = PriorityQueue()
        self.min_heap = PriorityQueue()

    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        """
        if self.max_heap.qsize() == 0:
            self.max_heap.put(-num)
            print('max, put', -num)
        else:
            max_left = -self.max_heap.get()
            n1 = max_left
            n2 = num
            if max_left > num:
                n1 = num
                n2 = max_left
            self.max_heap.put(-n1)
            print('max, put', -n1)
            if self.min_heap.qsize() > 0:
                min_right = self.min_heap.get()
                if n2 > min_right:
                    tmp = min_right
                    min_right = n2
                    n2 = tmp
                self.min_heap.put(min_right)
                print('min, put', min_right)
            if self.max_heap.qsize() > self.min_heap.qsize():
                self.min_heap.put(n2)
                print('min, put', n2)
            else:
                self.max_heap.put(-n2)
                print('max, put', -n2)

    def findMedian(self):
        """
        :rtype: float
        """
        if self.max_heap.qsize() > self.min_heap.qsize():
            med = -self.max_heap.get()
            self.max_heap.put(-med)
            print('max', med)
            return med
        else:
            left_max = -self.max_heap.get()
            self.max_heap.put(-left_max)
            right_min = self.min_heap.get()
            self.min_heap.put(right_min)
            print('max', left_max, 'min', right_min)
            return (left_max + right_min) / 2


# Your MedianFinder object will be instantiated and called as such:
obj = MedianFinder()
obj.addNum(1)
obj.addNum(2)
print(obj.findMedian())
obj.addNum(3)
print(obj.findMedian())
