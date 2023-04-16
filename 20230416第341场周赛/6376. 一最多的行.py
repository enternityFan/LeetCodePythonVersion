#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Project ：LeetCodePthonVersion 
@File ：6376. 一最多的行.py
@Author ：HuntingGame
@Date ：2023-04-16 10:30 
C'est la vie!!! enjoy ur day :D
'''
from typing import List


class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        ans = [-1,-1]
        minans = 0
        for i in range(len(mat)):
            tmp = sum(mat[i])
            if tmp >= ans[1]:
                ans[0] = i if (tmp !=1 ) or (tmp == 1 and ans[-1] == -1) else ans[0]
                ans[1] = tmp




        return ans


