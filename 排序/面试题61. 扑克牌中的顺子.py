#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Project ：LeetCodePthonVersion 
@File ：面试题61. 扑克牌中的顺子.py
@Author ：HuntingGame
@Date ：2023-03-07 13:43 
C'est la vie!!! enjoy ur day :D
'''
from typing import List


class Solution:
    def isStraight(self, nums: List[int]) -> bool:
        nums.sort()
        numZero = 0#0的数目
        flag = 0#连续的数
        for i in range(len(nums)):
            if nums[i] == 0:
                numZero +=1
            elif flag == 0 or nums[i] == nums[i-1]:
                flag +=1
            else:
                #TODO
                pass
