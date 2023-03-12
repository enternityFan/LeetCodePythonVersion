#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Project ：LeetCodePthonVersion 
@File ：6317. 统计美丽子数组数目.py
@Author ：HuntingGame
@Date ：2023-03-12 10:36 
C'est la vie!!! enjoy ur day :D
'''
import collections
from typing import List


class Solution:
    def beautifulSubarrays(self, nums: List[int]) -> int:
        """
        美丽子数组满足异或为0
        :param nums:
        :return:
        """
        mydict = {}# i:0..i-1异或值
        target = collections.defaultdict(int)# 异或值:数目
        tmp = 0
        ans = 0
        for i in range(len(nums)):
            mydict[i] = tmp
            target[tmp] +=1
            if tmp ^ nums[i] in target:
                ans +=target[tmp ^ nums[i]]



            tmp ^=nums
        return ans