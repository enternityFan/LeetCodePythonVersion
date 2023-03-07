#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Project ：LeetCodePthonVersion 
@File ：剑指 Offer 56 - I. 数组中数字出现的次数.py
@Author ：HuntingGame
@Date ：2023-03-07 18:22 
C'est la vie!!! enjoy ur day :D
'''
from typing import List


class Solution:
    def singleNumbers(self, nums: List[int]) -> List[int]:

        n = 0
        for c in nums:
            n ^=c
        rightOne = n & (~n + 1) #得到最右的rightOne
        a,b= 0,0
        for c in nums:
            if c & rightOne == rightOne:
                a ^=c
            else:
                b ^=c

        return [a,b]