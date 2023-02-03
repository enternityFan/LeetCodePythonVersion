#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Project ：LeetCodePthonVersion 
@File ：75. 颜色分类.py
@Author ：HuntingGame
@Date ：2023-02-03 14:28 
C'est la vie!!! enjoy ur day :D
'''
from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        less = -1#0的右边界
        more = len(nums)#2的左边界
        idx = 0#1的右边界
        while idx < more:
            if nums[idx] == 1:
                idx +=1
            elif nums[idx] == 0:
                nums[idx],nums[less+1] = nums[less+1],nums[idx]
                less +=1
                idx +=1
            else:
                nums[idx],nums[more-1] = nums[more-1],nums[idx]
                more -=1
        print(nums)

print(Solution().sortColors([2,0,2,1,1,0]))






