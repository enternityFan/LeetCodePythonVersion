#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2022/10/22 21:24
# @Author  : HuntingGame
# @FileName: 1090. 受标签影响的最大值.py
# @Software: PyCharm
# C'est la vie. Enjoy ur day ! :D
from typing import List


class Solution:
    def largestValsFromLabels(self, values: List[int], labels: List[int], numWanted: int, useLimit: int) -> int:
        values,labels = zip(*sorted(zip(values,labels),key=lambda x:x[0],reverse=True))
        ans=[]
        label_set = {}
        n = len(values)
        for i in range(n):
            if labels[i] not in label_set:
                label_set[labels[i]] = 1
                ans.append(values[i])
            elif label_set[labels[i]] < useLimit:
                ans.append(values[i])
                label_set[labels[i]] +=1
            if len(ans) == numWanted:
                break

        return sum(ans)


print(Solution().largestValsFromLabels([5,4,3,2,1],[1,3,3,3,2],3,2))