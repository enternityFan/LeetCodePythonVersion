# @Time : 2022-07-29 20:33
# @Author : Phalange
# @File : 1282. 用户分组.py
# @Software: PyCharm
# C'est la vie,enjoy it! :D
from typing import List
import collections

class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        mydict = collections.defaultdict(list)
        res = []
        for i,each in enumerate(groupSizes):
            mydict[each].append(i)

        for key,value in mydict.items():
            if len(value) == key:
                res.append(value)
            else:
                times = int(len(value) / key)
                for i in range(times):
                    res.append(value[i*key:(i+1)*key])

        return res

