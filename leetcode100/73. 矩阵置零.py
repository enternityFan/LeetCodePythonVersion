#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Project ：LeetCodePthonVersion 
@File ：73. 矩阵置零.py
@Author ：HuntingGame
@Date ：2023-02-03 14:13 
C'est la vie!!! enjoy ur day :D
'''
from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row0Zero = False
        col0Zero = False
        i = 0
        j = 0
        for i in range(len(matrix[0])):
            if matrix[0][i] == 0:
                row0Zero = True
                break

        for i in range(len(matrix)):
            if matrix[i][0] == 0:
                col0Zero = True
                break

        for i in range(1,len(matrix)):
            for j in range(1,len(matrix[0])):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        for i in range(1,len(matrix)):
            for j in range(1,len(matrix[0])):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
        if row0Zero:
            for i in range(len(matrix[0])):
                matrix[0][i] = 0
        if col0Zero:
            for i in range(len(matrix)):
                matrix[i][0] = 0
        print(matrix)


matrix = [[1,1,1],[1,0,1],[1,1,1]]
print(Solution().setZeroes(matrix))