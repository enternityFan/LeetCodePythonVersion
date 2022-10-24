#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2022/10/22 21:10
# @Author  : HuntingGame
# @FileName: 945. 使数组唯一的最小增量.py
# @Software: PyCharm
# C'est la vie. Enjoy ur day ! :D
from typing import List


class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        nums.sort()
        ans = 0
        if len(nums) == 1:
            return 0
        for i in range(1,len(nums)):
            if nums[i] == nums[i-1]:
                ans +=1
                nums[i] +=1
            elif nums[i] < nums[i-1]:
                ans +=nums[i-1] - nums[i]+1
                nums[i] = nums[i-1] + 1


        return ans

