# @Time : 2022-07-30 18:23
# @Author : Phalange
# @File : 73. 矩阵置零.py
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
            # 行清零
            matrix[each[0]] = [0] * n
            # 列清零
            for i in range(m):
                matrix[i][each[1]] = 0


matrix = [[1,1,1],[1,0,1],[1,1,1]]
s =  Solution()
print(s.setZeroes(matrix))