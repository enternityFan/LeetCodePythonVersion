#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Project ：LeetCodePythonVersion 
@File ：1089. 复写零.py
@Author ：HuntingGame
@Date ：2022/9/22 8:57 
C'est la vie!!! :)
'''
from typing import List


class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """

        idx = []
        j = 0
        for i in range(len(arr)):
            if arr[i] == 0:
                idx.append(i)
        for i in idx:
            arr.insert(i+j,0)
            j+=1
            arr.pop()
