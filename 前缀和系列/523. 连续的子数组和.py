#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Project ：LeetCodePthonVersion 
@File ：523. 连续的子数组和.py
@Author ：HuntingGame
@Date ：2022-11-22 9:20 
C'est la vie!!! enjoy ur day :D
'''
from typing import List


class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:

        cur = 0
        ans = 0
        n = len(nums)
        if n == 1:
            return True if nums[0] % k == 0 else False
        for i in range(n):
            if nums[]



nums = [23, 2, 4, 6, 7]
k = 6
print(Solution().checkSubarraySum(nums,k))