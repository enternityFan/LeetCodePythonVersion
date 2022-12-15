#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Project ：LeetCodePthonVersion 
@File ：剑指 Offer II 101. 分割等和子集.py
@Author ：HuntingGame
@Date ：2022-12-15 13:03 
C'est la vie!!! enjoy ur day :D
'''
from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:

        if len(nums) == 1 or sum(nums)% 2 !=0:
            return False
        target = sum(nums) // 2
        if target in nums:
            return True
        # 0-1背包问题
        dp = [False] * (target+1)
        dp[0] = True
        for i,num in enumerate(nums):
            for j in range(target,num - 1,-1):
                dp[j] |=dp[j-num]
        return dp[target]

print(Solution().canPartition([1,2,1,2]))