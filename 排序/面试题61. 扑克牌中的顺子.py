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
        need = 0#需要的数目
        for i in range(len(nums)):
            if nums[i] == 0:
                numZero +=1
            elif flag == 0 or nums[i] == flag+1:
                flag = nums[i]
            else:
                need +=abs(nums[i] - flag-1)
                flag =nums[i]
        if numZero >= need:
            return True
        return False
print(Solution().isStraight([11,8,12,8,10]))

