#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Project ：LeetCodePthonVersion 
@File ：找出可整除性得分最大的整数.py
@Author ：HuntingGame
@Date ：2023-04-16 10:34 
C'est la vie!!! enjoy ur day :D
'''
import collections
from typing import List


class Solution:
    def maxDivScore(self, nums: List[int], divisors: List[int]) -> int:
        mydict = collections.defaultdict(list)
        maxval = -1
        for i in range(len(divisors)):
            tmp = 0
            for j in range(len(nums)):
                if nums[j] % divisors[i] == 0:
                    tmp +=1
            mydict[tmp].append(divisors[i])
            maxval = max(maxval,tmp)



        return min(mydict[maxval])