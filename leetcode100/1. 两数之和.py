#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Project ：LeetCodePthonVersion 
@File ：1. 两数之和.py
@Author ：HuntingGame
@Date ：2023-02-01 9:32 
C'est la vie!!! enjoy ur day :D
'''
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # 利用Hashmap来做
        mydict = {}
        for i in range(len(nums)):
            if target - nums[i] not in mydict:
                mydict[nums[i]] = i
            else:
                return [i,mydict[target - nums[i]]]


print(Solution().twoSum([2,7,11,15],9))
