class Iterator(object):
    def __init__(self, nums):
        """
        Initializes an iterator object to the beginning of a list.
        :type nums: List[int]
        """
        self.__nums = nums
        self.__current_index = -1

    def hasNext(self):
        """
        Returns true if the iteration has more elements.
        :rtype: bool
        """
        return self.__current_index + 1 < len(self.__nums)

    def next(self):
        """
        Returns the next element in the iteration.
        :rtype: int
        """
        if self.hasNext():
            self.__current_index += 1
            return self.__nums[self.__current_index]
        return None

class PeekingIterator(object):
    def __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        self.__iterator = iterator
        self.__has_peeked = False
        self.__next_value = None

    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        if not self.__has_peeked:
            self.__next_value = self.__iterator.next()
            self.__has_peeked = True
        return self.__next_value

    def next(self):
        """
        :rtype: int
        """
        if self.__has_peeked:
            self.__has_peeked = False
            return self.__next_value
        return self.__iterator.next()

    def hasNext(self):
        """
        :rtype: bool
        """
        if self.__has_peeked:
            return True
        return self.__iterator.hasNext()

# Your PeekingIterator object will be instantiated and called as such:
testCases = [
        [1, 2, 3],
        [],
        [1],
        [0, 0, 1, 1, 3]
        ]
for nums in testCases:
    print('TestCase:', nums)
    iter = PeekingIterator(Iterator(nums))
    while iter.hasNext():
        valp = iter.peek()   # Get the next element but not advance the iterator.
        valn = iter.next()   # Should return the same value as [val].
        print(valp, valn)
    valp = iter.peek()   # Get the next element but not advance the iterator.
    valn = iter.next()   # Should return the same value as [val].
    print(valp, valn)

