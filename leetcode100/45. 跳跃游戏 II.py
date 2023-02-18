#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Project ：LeetCodePthonVersion 
@File ：45. 跳跃游戏 II.py
@Author ：HuntingGame
@Date ：2023-02-02 20:52 
C'est la vie!!! enjoy ur day :D
'''
from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        """
        这个题三个变量就行了
        step:表示至少要跳几次到i位置
        cur:跳到步数不超过step步的情况下，最右能到哪
        next:跳的步数不超过step+1步的情况下，最右在哪里。
        :param nums:
        :return:
        """
        step = 0
        cur = 0
        next = nums[0]
        for i in range(len(nums)):
            if i > cur:
                step +=1
                cur = next
            next = max(next,i+nums[i])
            # 下面两行代码不能加，一加纠错。
            # if next >=len(nums):
            #     return step+1

        return step













