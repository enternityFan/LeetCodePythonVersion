#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Project ：LeetCodePthonVersion 
@File ：152. 乘积最大子数组.py
@Author ：HuntingGame
@Date ：2023-02-06 18:50 
C'est la vie!!! enjoy ur day :D
'''
from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        """
        子数组问题还是考虑以i位置结尾
        1)只有[i]
        2）不止以[i]：2.1)最大的[i-1]累乘积。 * i.2.2)最小的[i-1]累成绩 * i
        :param nums:
        :return:
        """
        ans = nums[0]
        minval = nums[0]
        maxval = nums[0]
        for i in range(1,len(nums)):
            curmin = min(nums[i],min(minval * nums[i],maxval * nums[i]))
            curmax = max(nums[i],max(minval * nums[i],maxval * nums[i]))
            minval = curmin
            maxval = curmax
            ans = max(ans,maxval)

        return ans