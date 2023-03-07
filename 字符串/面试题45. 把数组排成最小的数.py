#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Project ：LeetCodePthonVersion 
@File ：面试题45. 把数组排成最小的数.py
@Author ：HuntingGame
@Date ：2023-03-07 18:14 
C'est la vie!!! enjoy ur day :D
'''
import functools
from typing import List


class Solution:
    def minNumber(self, nums: List[int]) -> str:
        def sort_rule(x, y):
            a, b = x + y, y + x
            if a > b:
                return 1
            elif a < b:
                return -1
            else:
                return 0

        for i in range(len(nums)):
            nums[i] = str(nums[i])
        nums.sort(key=functools.cmp_to_key(sort_rule))
        print(nums)

        return "".join(nums)

a = [3,30,34,5,9]
print(Solution().minNumber(a))