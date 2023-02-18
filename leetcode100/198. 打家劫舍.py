#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Project ：LeetCodePthonVersion 
@File ：198. 打家劫舍.py
@Author ：HuntingGame
@Date ：2023-02-07 21:11 
C'est la vie!!! enjoy ur day :D
'''
from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        下面还有原始的dp的方式
        dp[i] 是0到i能劫的最大钱数。
        :param nums:
        :return:
        """
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        pre2 = nums[0]
        pre1 = max(nums[0],nums[1])
        for i in range(2,len(nums)):
            cur = max(pre1,nums[i] + pre2)
            pre2 = pre1
            pre1 = cur

        return pre1


class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        dp[i] 是0到i能劫的最大钱数。
        :param nums:
        :return:
        """
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        dp = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[0],nums[1])
        for i in range(2,len(nums)):
            dp[i] = max(dp[i-1],dp[i-2] + nums[i])

        return dp[-1]
