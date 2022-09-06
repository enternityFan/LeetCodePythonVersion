# @Time : 2022-09-06 13:21
# @Author : Phalange
# @File : 1636. 按照频率将数组升序排序.py
# @Software: PyCharm
# C'est la vie,enjoy it! :D
import collections
from typing import List



class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        mycounter = collections.Counter(nums)
        mylist = [list(mycounter.keys()),list(mycounter.values())]
        mylist = sorted(mylist,key=lambda x:(x[1],-x[0]))
        ans = []
        for i in range(len(mylist)):
            pass

        return mylist

print(Solution().frequencySort( [-1,1,-6,4,5,-6,1,4,1]))