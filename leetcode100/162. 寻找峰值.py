#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Project ：LeetCodePthonVersion 
@File ：162. 寻找峰值.py
@Author ：HuntingGame
@Date ：2023-02-07 19:28 
C'est la vie!!! enjoy ur day :D
'''
from typing import List


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        """
        二分来做，首先看0和N-1位置是不是局部最高点，如果是直接返回，否则：
        如果左边上升趋势，右边是下降趋势，如果M位置大于左边和右边，那就返回；

        :param nums:
        :return:
        """
        n = len(nums)
        if n < 2:
            return 0
        if nums[0] > nums[1]:
            return 0
        if nums[n - 1] > nums[n-2]:
            return n-1
        L = 1
        R = n-2
        M = 0
        while L < R:
            M = (L+ R) // 2
            if nums[M-1] < nums[M] and nums[M] > nums[M +1]:
                return M
            elif nums[M - 1] > nums[M]:
                R = M - 1
            else:
                L = M + 1

        return L# 最后把唯一剩下的位置返回。