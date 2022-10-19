#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Project ：LeetCodePthonVersion 
@File ：2190. 数组中紧跟 key 之后出现最频繁的数字.py
@Author ：HuntingGame
@Date ：2022-10-18 12:43 
C'est la vie!!! enjoy ur day :D
'''
import collections
from typing import List


class Solution:
    def mostFrequent(self, nums: List[int], key: int) -> int:
        targets = collections.defaultdict(int)
        for i in range(len(nums)-1):
            if nums[i] == key:
                targets[nums[i+1]] +=1
        maxcnt = max(targets.values())
        for key,val in targets.items():
            if val == maxcnt:
                return key
