# @Time : 2022-08-13 17:43
# @Author : Phalange
# @File : 2032. 至少在两个数组中出现的值.py
# @Software: PyCharm
# C'est la vie,enjoy it! :D
import collections
from typing import List


class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        mymap = collections.defaultdict(int)
        ans = []
        for each in set(nums1):
            mymap[each] +=1
        for each in set(nums2):
            if mymap[each] == 1:
                ans.append(each)
                mymap[each] = 0
            else:
                mymap[each] +=1
        for each in set(nums3):
            if mymap[each] == 1:
                ans.append(each)
        return ans