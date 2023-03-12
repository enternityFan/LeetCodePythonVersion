#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Project ：LeetCodePthonVersion 
@File ：剑指 Offer II 074. 合并区间.py
@Author ：HuntingGame
@Date ：2023-03-12 12:24 
C'est la vie!!! enjoy ur day :D
'''
from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x:x[0])
        ans = []
        if len(intervals) == 1:
            return intervals
        L = intervals[0][0]
        R = intervals[0][1]
        for i in range(1,len(intervals)):
            if intervals[i][0] > R:
                #说明没有重叠的地方
                ans.append([L,R])
                L = intervals[i][0]
                R = intervals[i][1]
            elif intervals[i][1] <=R:
                #被包括了
                continue
            else:
                R = intervals[i][1]
        ans.append([L,R])
        return ans