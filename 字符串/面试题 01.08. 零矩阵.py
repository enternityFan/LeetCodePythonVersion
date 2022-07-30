# @Time : 2022-07-29 21:47
# @Author : Phalange
# @File : 面试题 01.08. 零矩阵.py
# @Software: PyCharm
# C'est la vie,enjoy it! :D
from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])
        idx = []
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    idx.append([i,j])

        for each in idx:
            # 清0行
            matrix[each[0]] = 0
            # 清零列
            for i in range(m):
                matrix[i][each[1]] = 0



