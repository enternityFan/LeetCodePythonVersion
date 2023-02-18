#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Project ：LeetCodePthonVersion 
@File ：922. 按奇偶排序数组 II.py
@Author ：HuntingGame
@Date ：2022-12-27 8:03 
C'est la vie!!! enjoy ur day :D
'''
from typing import List


class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        n = len(nums)
        endpt = n-1#一直指最后一个位置
        opt = 1 #一直指奇数位置
        ept = 0 #一直指偶数

        while ept < n and opt < n:
            if nums[endpt] % 2 == 0:
                nums[endpt],nums[ept] = nums[ept],nums[endpt]
                ept +=2
            else:
                nums[endpt],nums[opt] = nums[opt],nums[endpt]
                opt +=2
        return nums
