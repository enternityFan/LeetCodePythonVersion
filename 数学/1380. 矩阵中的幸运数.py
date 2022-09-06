# @Time : 2022-09-06 12:55
# @Author : Phalange
# @File : 1380. 矩阵中的幸运数.py
# @Software: PyCharm
# C'est la vie,enjoy it! :D
from typing import List


class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        maxVal = []
        minVal = []
        rows = len(matrix)
        cols = len(matrix[0])
        for r in range(rows):
            minVal.append(min(matrix[r]))

        for c in range(cols):
            tmp = [matrix[i][c] for i in range(rows) ]
            maxVal.append(max(tmp))

        return list(set(minVal)&set(maxVal))

matrix = [[1,10,4,2],[9,3,8,7],[15,16,17,12]]
print(Solution().luckyNumbers(matrix))