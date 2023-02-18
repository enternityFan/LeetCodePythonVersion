#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Project ：LeetCodePthonVersion 
@File ：283. 移动零.py
@Author ：HuntingGame
@Date ：2023-02-08 19:29 
C'est la vie!!! enjoy ur day :D
'''
from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        还是垃圾区的事。
        b遇到不是0的，就跟a的下一个位置交换，然后a++
        """
        a = 0
        for b in range(len(nums)):
            if nums[b] !=0:
                nums[a],nums[b] = nums[b],nums[a]
                a +=1
