# @Time : 2022-08-20 17:10
# @Author : Phalange
# @File : 1436. 旅行终点站.py
# @Software: PyCharm
# C'est la vie,enjoy it! :D
import collections
from typing import List


class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        mydict = collections.defaultdict(str)
        for each in paths:
            mydict[each[0]] = each[1]

        key = paths[0][0]
        while key in mydict:
            key = mydict[key]

        return key