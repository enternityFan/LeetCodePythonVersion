#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2022/10/16 10:30
# @Author  : HuntingGame
# @FileName: 6204. 与对应负数同时存在的最大正整数.py
# @Software: PyCharm
# C'est la vie. Enjoy ur day ! :D
from typing import List


class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        nums.sort()
        maxval = -1
        for i in range(len(nums)):
            if nums[i] >0:
                break
            if maxval == -1 and -nums[i] in nums:
                maxval = max(maxval,-nums[i])

            if maxval !=-1:
                break
        return maxval

