#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Project ：LeetCodePthonVersion 
@File ：面试题 10.09. 排序矩阵查找.py
@Author ：HuntingGame
@Date ：2022-11-18 8:27 
C'est la vie!!! enjoy ur day :D
'''
from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])

        r = 0
        c = n - 1
        while (r < m and n >-1):
            if matrix[r][c] == target:
                return True
            elif matrix[r][c] > target:
                c -=1
            else:
                r +=1
        return False