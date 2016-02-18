class MedianFinder:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.nums = []

    def addNum(self, num):
        """
        Adds a num into the data structure.
        :type num: int
        :rtype: void
        """
        length = len(self.nums)
        if length == 0:
            self.nums.append(num)
        else:
            lower, upper = 0, length
            while lower < upper:
                middle = lower + ((upper - lower) // 2)
                if (self.nums[middle] < num):
                    lower = middle + 1
                else:
                    upper = middle
            self.nums.insert(lower, num)

    def findMedian(self):
        """
        Returns the median of current data stream
        :rtype: float
        """
        length = len(self.nums)
        if length % 2 == 1:
            return self.nums[length // 2]
        return (self.nums[length // 2] + self.nums[length // 2 - 1]) / 2.0

# Your MedianFinder object will be instantiated and called as such:
mf = MedianFinder()
mf.addNum(1)
print(mf.findMedian())
mf.addNum(2)
print(mf.findMedian())
mf.addNum(-1)
print(mf.findMedian())
print(mf.findMedian())
mf.addNum(1)
print(mf.findMedian())
mf.addNum(2)
print(mf.findMedian())
mf.addNum(3)
print(mf.findMedian())
mf.addNum(6)
print(mf.findMedian())
mf.addNum(9)
print(mf.findMedian())
mf.addNum(0)
print(mf.findMedian())
mf.addNum(-2)
print(mf.findMedian())

