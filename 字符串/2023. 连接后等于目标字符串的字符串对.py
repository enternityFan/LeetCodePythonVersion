#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Project ：LeetCodePthonVersion 
@File ：2023. 连接后等于目标字符串的字符串对.py
@Author ：HuntingGame
@Date ：2022-11-07 9:09 
C'est la vie!!! enjoy ur day :D
'''
from typing import List


class Solution:
    def numOfPairs(self, nums: List[str], target: str) -> int:
        ans = 0

        for i in range(len(nums)):
            if len(nums[i]) > len(target) or nums[i] !=target[:len(nums[i])]:
                continue
            for j in range(len(nums)):
                if i == j:
                    continue
                if nums[i] + nums[j] == target:
                    ans +=1


        return ans
