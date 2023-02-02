#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Project ：LeetCodePthonVersion 
@File ：55. 跳跃游戏.py
@Author ：HuntingGame
@Date ：2023-02-02 20:57 
C'est la vie!!! enjoy ur day :D
'''
from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:

        ans = 0# 目前为止能到的最右的位置。
        n = len(nums)
        for i in range(n):
            if i > ans:
                # 说明到不了i这个位置。
                return False
            ans = max(ans,i+nums[i])

        return True