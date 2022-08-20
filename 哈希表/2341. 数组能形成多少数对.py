# @Time : 2022-08-20 17:19
# @Author : Phalange
# @File : 2341. 数组能形成多少数对.py
# @Software: PyCharm
# C'est la vie,enjoy it! :D
import collections
from typing import List


class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        mymap = collections.defaultdict(int)
        times = 0
        for i in range(len(nums)):
            mymap[nums[i]] +=1
            if mymap[nums[i]] == 2:
                mymap.pop(nums[i])
                times = times+1

        return [times,len(mymap.keys())]