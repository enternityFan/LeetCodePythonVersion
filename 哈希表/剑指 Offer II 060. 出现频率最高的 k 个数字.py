# @Time : 2022-07-30 17:35
# @Author : Phalange
# @File : 剑指 Offer II 060. 出现频率最高的 k 个数字.py
# @Software: PyCharm
# C'est la vie,enjoy it! :D
from typing import List
import collections

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mydict = {}
        for each in nums:
            if each in mydict:
                mydict[each] +=1
            else:
                mydict[each] = 1
        mydict = sorted(mydict.items(),key=lambda x:x[1],reverse=True)#按照值进行排序

        res = []
        for i,each in enumerate(mydict):
            if i < k:
                res.append(each[0])
            else:
                break
        return res


