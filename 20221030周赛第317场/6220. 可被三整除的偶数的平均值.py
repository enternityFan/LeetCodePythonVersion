#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Project ：LeetCodePthonVersion 
@File ：6220. 可被三整除的偶数的平均值.py
@Author ：HuntingGame
@Date ：2022-10-30 10:30 
C'est la vie!!! enjoy ur day :D
'''

class Solution:
    def averageValue(self, nums: List[int]) -> int:
        ans = []
        for i in range(len(nums)):
            if nums[i] % 2 == 0 and nums[i] % 3 == 0:
                ans.append(nums[i])
        if len(ans) == 0:
            return 0
        return sum(ans) // len(ans)