#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Project ：LeetCodePthonVersion 
@File ：287. 寻找重复数.py
@Author ：HuntingGame
@Date ：2023-02-08 11:10 
C'est la vie!!! enjoy ur day :D
'''
from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return -1
        slow = nums[0]
        fast = nums[[nums[0]]]
        while slow !=fast:
            slow = nums[slow]
            fast = nums[nums[fast]]
        fast = 0
        while slow !=fast:
            fast = nums[fast]
            slow = nums[slow]

        return slow