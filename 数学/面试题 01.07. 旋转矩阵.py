# @Time : 2022-07-29 17:16
# @Author : Phalange
# @File : 面试题 01.07. 旋转矩阵.py
# @Software: PyCharm
# C'est la vie,enjoy it! :D
from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        for i in range(n // 2):
            for j in range((n + 1) // 2):
                matrix[i][j], matrix[n - j - 1][i], matrix[n - i - 1][n - j - 1], matrix[j][n - i - 1] \
                    = matrix[n - j - 1][i], matrix[n - i - 1][n - j - 1], matrix[j][n - i - 1], matrix[i][j]

matrix = [[1,2,3],[4,5,6],[7,8,9]]
matrix2 = [[1,2],[3,4]]
matrix3 = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
s = Solution()
print(s.rotate(matrix2))


