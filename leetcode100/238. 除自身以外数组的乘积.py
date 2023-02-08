#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Project ：LeetCodePthonVersion 
@File ：238. 除自身以外数组的乘积.py
@Author ：HuntingGame
@Date ：2023-02-08 13:10 
C'est la vie!!! enjoy ur day :D
'''
from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        做一个all把所有不是0的数的积存起来。cnt统计0有多少个
        如果cnt大于等于2，那么肯定全是0
        :param nums:
        :return:
        """
        all = 1
        zeros = 0
        for each in nums:
            if each == 0:
                zeros +=1
            else:
                all *=each

        if zeros > 1:
            for i in range(len(nums)):
                nums[i] = 0

        else:
            for i in range(len(nums)):
                nums[i] = (all // nums[i]) if zeros == 0 else all if nums[i] == 0 else 0

        return nums
