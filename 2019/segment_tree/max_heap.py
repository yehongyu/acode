#coding=utf-8

class MaxHeap(object):

    def __init__(self):
        self._data = []
        self._count = len(self._data)

    def size(self):
        return self._count

    def isEmpty(self):
        return self._count == 0

    def add(self, item):
        # 插入元素入堆
        self._data.append(item)
        self._count += 1
        self._shiftup(self._count-1)

    def pop(self):
        # 出堆
        if self._count > 0:
            ret = self._data[0]
            self._data[0] = self._data[self._count-1]
            self._count -= 1
            self._shiftDown(0)
            return ret

    def top(self):
        return self._data[0]

    def _shiftup(self, index):
        # 上移self._data[index]，以使它不大于父节点
        parent = (index-1)>>1
        while index > 0 and self._data[parent] < self._data[index]:
            # swap
            self._data[parent], self._data[index] = self._data[index], self._data[parent]
            index = parent
            parent = (index-1)>>1

    def _shiftDown(self, index):
        # 上移self._data[index]，以使它不小于子节点
        j = (index << 1) + 1
        while j < self._count :
            # 有子节点
            if j+1 < self._count and self._data[j+1] > self._data[j]:
                # 有右子节点，并且右子节点较大
                j += 1
            if self._data[index] >= self._data[j]:
                # 堆的索引位置已经大于两个子节点，不需要交换了
                break
            self._data[index], self._data[j] = self._data[j], self._data[index]
            index = j
            j = (index << 1) + 1

if __name__ == '__main__':
    maxheap = MaxHeap()
    maxheap.add(6)
    print maxheap.top()
    maxheap.add(8)
    print maxheap.top()
    maxheap.add(9)
    print maxheap.top()
    maxheap.add(9)
    print maxheap.top()
    maxheap.add(3)
    print maxheap.top()
    print 'pop'
    maxheap.pop()
    print maxheap.top()
    print 'pop'
    maxheap.pop()
    print maxheap.top()

