#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Project ：LeetCodePthonVersion 
@File ：136. 只出现一次的数字.py
@Author ：HuntingGame
@Date ：2023-02-06 10:00 
C'est la vie!!! enjoy ur day :D
'''
from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ans = 0
        for i in nums:
            ans ^=i
        return ans