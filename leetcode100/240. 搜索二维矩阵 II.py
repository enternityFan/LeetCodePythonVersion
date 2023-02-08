#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Project ：LeetCodePthonVersion 
@File ：240. 搜索二维矩阵 II.py
@Author ：HuntingGame
@Date ：2023-02-08 13:16 
C'est la vie!!! enjoy ur day :D
'''
from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """
        从右上角开始找，如果小于target，那就往下走，大的话那就往左走
        :param matrix:
        :param target:
        :return:
        """
        N = len(matrix)
        M = len(matrix[0])
        if M == 0 or N == 0 :
            return False
        row = 0
        col = M-1
        while row < N and col >=0:
            if matrix[row][col] > target:
                col -=1
            elif matrix[row][col] < target:
                row +=1
            else:
                return True

        return False









