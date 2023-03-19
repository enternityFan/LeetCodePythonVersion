#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Project ：LeetCodePthonVersion 
@File ：6351. 标记所有元素后数组的分数.py
@Author ：HuntingGame
@Date ：2023-03-18 23:10 
C'est la vie!!! enjoy ur day :D
'''
import collections
import heapq
from typing import List


class Solution:
    def findScore(self, nums: List[int]) -> int:
        n = len(nums)

        mynums = [[nums[i],i] for i in range(n)]
        heapq.heapify(mynums)
        ans = 0
        myset = set()
        while mynums !=[]:
            val,idx = heapq.heappop(mynums)
            #print(val,idx)
            if idx not in myset:
                # 未被标记
                ans +=val
                myset.add(idx)
                if idx !=0:
                    myset.add(idx-1)
                if idx != n-1:
                    myset.add(idx +1)







        return ans
print(Solution().findScore([2,7,6]))