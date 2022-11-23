#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Project ：LeetCodePthonVersion 
@File ：300. 最长递增子序列.py
@Author ：HuntingGame
@Date ：2022-11-22 8:24 
C'est la vie!!! enjoy ur day :D
'''
import bisect
from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0] * n
        ends = [0]
        ends[0] = nums[0]
        dp[0] = 1
        for i in range(1,n):
            j = bisect.bisect_left(ends,nums[i])
            if j < len(ends):
                ends[j] = nums[i]
            else:
                ends.append(nums[i])


        return len(ends)

        # 下面的是打印的
        # len2 = 0
        # index = 0
        # for i in range(len(dp)):
        #     if dp[i] > len2:
        #         len2 = dp[i]
        #         index = i
        #
        # lis = [0] * len2
        # lis[-1] = nums[index]
        # len2 -=1
        # for i in range(index,-1,-1):
        #     if nums[i] < nums[index] and dp[i] == dp[index]:
        #         lis[len2] = nums[i]
        #         len2 -=1
        #         index = i
        #
        # return lis
print(Solution().lengthOfLIS([1,2,3]))