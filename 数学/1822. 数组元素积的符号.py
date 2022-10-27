#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Project ：LeetCodePthonVersion 
@File ：1822. 数组元素积的符号.py
@Author ：HuntingGame
@Date ：2022-10-27 18:14 
C'est la vie!!! enjoy ur day :D
'''
class Solution:
    def arraySign(self, nums: List[int]) -> int:
        ans = 1
        for i in range(len(nums)):
            if nums[i] == 0:
                return 0
            elif nums[i] < 0:
                ans *=-1
        return ans
