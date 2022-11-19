#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Project ：LeetCodePthonVersion 
@File ：1481. 不同整数的最少数目.py
@Author ：HuntingGame
@Date ：2022-11-14 11:09 
C'est la vie!!! enjoy ur day :D
'''
import collections
from typing import List


class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:

        mydict = collections.defaultdict(int)
        for i in range(len(arr)):
            mydict[arr[i]] +=1
        keys, values = zip(*sorted(zip(list(mydict.keys()), list(mydict.values())), key=lambda x: (x[1], -x[0])))
        keys = list(keys)
        values = list(values)
        i = 0

        ans = 0
        while k>0:
            k -=values[i]
            i +=1




        if k <0:
            ans = len(values) - i +1
        else:
            ans = len(values) - i
        return ans

print(Solution().findLeastNumOfUniqueInts([5,5,4],1))


