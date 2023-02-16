#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Project ：LeetCodePthonVersion 
@File ：2562. 找出数组的串联值.py
@Author ：HuntingGame
@Date ：2023-02-16 15:02 
C'est la vie!!! enjoy ur day :D
'''
from typing import List


class Solution:
    def findTheArrayConcVal(self, nums: List[int]) -> int:
        ans = 0
        L = 0
        R = len(nums)-1
        while L<R:
            if L!=R:
                #说明有两个字
                ans +=eval(str(nums[L]) + str(nums[R]))
                L +=1
                R -=1
        if L == R:
            ans +=nums[L]
        return ans
