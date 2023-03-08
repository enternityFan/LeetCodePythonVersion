#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Project ：LeetCodePthonVersion 
@File ：523. 连续的子数组和.py
@Author ：HuntingGame
@Date ：2022-11-22 9:20 
C'est la vie!!! enjoy ur day :D
'''
import collections
from typing import List


class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        """
        当两个数除以某个数的余数相等，那么二者相减后肯定可以被该数整除
        计算这个题需要用到上面的同余定理
        :param nums:
        :param k:
        :return:
        """
        yudict = set()#存放余数
        tmp = 0
        for i in range(len(nums)):
            last = tmp #记录上一个数的前缀和，来实现长度必须大于等于2的要求
            tmp +=nums[i]
            tmp %=k
            if tmp in yudict:
                return True
            yudict.add(last)

        return False



nums = [23, 2, 6, 4, 7]
#nums=[0]
k = 6
print(Solution().checkSubarraySum(nums,k))