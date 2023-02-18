#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Project ：LeetCodePthonVersion 
@File ：53. 最大子数组和.py
@Author ：HuntingGame
@Date ：2023-02-03 11:07 
C'est la vie!!! enjoy ur day :D
'''
from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """
        1)只含[i]
        2)不止含有[i]
        dp[0] = nums[0]
        p1 = nums[i]
        p2 = nums[i] + dp[i-1]
        dp[i] = max(p1,p2)
        ans = dp[-1]
        下面的代码相当于是空间优化后的。
        :param nums:
        :return:
        """
        cur = 0
        maxval = -2 **31
        for i in range(len(nums)):
            cur +=nums[i]
            maxval = max(maxval,cur)
            cur = 0 if cur < 0 else cur

        return maxval