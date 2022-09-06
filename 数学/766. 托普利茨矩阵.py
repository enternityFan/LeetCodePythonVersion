# @Time : 2022-09-06 13:08
# @Author : Phalange
# @File : 766. 托普利茨矩阵.py
# @Software: PyCharm
# C'est la vie,enjoy it! :D
from typing import List

"""
1 2
2 2
"""


class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        flag = True
        rows = len(matrix)
        cols = len(matrix[0])

        if rows == 1 or cols == 1:
            return flag

        for r in range(1, rows):
            for c in range(1,cols):
                if matrix[r][c] != matrix[r-1][c-1]:
                    flag = False
                    break

        return flag

matrix = [[1,2],[2,2]]
print(Solution().isToeplitzMatrix(matrix))