# @Time : 2022-07-29 21:53
# @Author : Phalange
# @File : 2150. 找出数组中的所有孤独数字.py
# @Software: PyCharm
# C'est la vie,enjoy it! :D
from typing import List


class Solution:
    def findLonely(self, nums: List[int]) -> List[int]:
        mydict = {}
        for each in nums:
            if each not in mydict:
                mydict[each] = 1
            else:
                mydict[each] +=1
        arr = []
        for k,v in mydict.items():
            if v == 1 and ((k+1) not in mydict and (k-1) not in mydict):
                arr.append(k)

        return arr

