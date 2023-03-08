#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Project ：LeetCodePthonVersion 
@File ：560. 和为 K 的子数组.py
@Author ：HuntingGame
@Date ：2023-03-08 14:48 
C'est la vie!!! enjoy ur day :D
'''
import collections
from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        mydict = {}#i:0..i-1的前缀和
        mydict2 = collections.defaultdict(int)#target:数目
        tmp = 0
        ans = 0
        for i in range(len(nums)):
            mydict[i] = tmp
            mydict2[tmp] += 1
            tmp +=nums[i]
            if nums[i] + mydict[i] - k in mydict2:
                ans +=mydict2[nums[i] + mydict[i] - k]
        return ans

print(Solution().subarraySum([1,-1,0],0))