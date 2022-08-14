# @Time : 2022-08-14 10:41
# @Author : Phalange
# @File : 6149. 边积分最高的节点.py
# @Software: PyCharm
# C'est la vie,enjoy it! :D
import collections
from typing import List


class Solution:
    def edgeScore(self, edges: List[int]) -> int:
        maxValue = 0
        maxIdx = -1 #表示无效
        mymap = collections.defaultdict(int)
        n = len(edges)
        for i in range(n):
            mymap[edges[i]] +=i
            if maxValue <mymap[edges[i]]:
                maxValue = mymap[edges[i]]

                maxIdx = edges[i]
            elif maxValue == mymap[edges[i]] and maxIdx > edges[i]:
                maxIdx = edges[i]

        return maxIdx