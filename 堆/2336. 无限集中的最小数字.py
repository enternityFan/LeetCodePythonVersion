# @Time : 2022-08-03 10:49
# @Author : Phalange
# @File : 2336. 无限集中的最小数字.py
# @Software: PyCharm
# C'est la vie,enjoy it! :D
import collections
import sys
import heapq

class SmallestInfiniteSet:

    def __init__(self):

        self.arr = [i for i in range(1,1001)]
        heapq.heapify(self.arr)
        self.map = set(self.arr)



    def popSmallest(self) -> int:
        self.map.remove(self.arr[0])
        return heapq.heappop(self.arr)


    def addBack(self, num: int) -> None:
        if num in self.map:
            return

        heapq.heappush(self.arr,num)
        self.map.add(num)


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)
